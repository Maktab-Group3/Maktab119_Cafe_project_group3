// 1. تنظیم یا ایجاد کوکی
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

// 2. دریافت مقدار کوکی
function getCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.indexOf(nameEQ) === 0) {
            return cookie.substring(nameEQ.length, cookie.length);
        }
    }
    return null;
}

// 3. آپدیت کوکی (افزودن آیتم یا تغییر تعداد آن)
function updateCookie(itemName, quantity) {
    const cookieName = "menuItems"; // نام کوکی
    let menuData = getCookie(cookieName);

    if (!menuData) {
        // اگر کوکی وجود نداشت، یک آبجکت جدید می‌سازیم
        menuData = {};
    } else {
        menuData = JSON.parse(menuData); // تبدیل کوکی به آبجکت جاوااسکریپت
    }

    // آپدیت یا اضافه کردن آیتم
    if (menuData[itemName]) {
        menuData[itemName] += quantity; // تعداد را اضافه می‌کنیم
    } else {
        menuData[itemName] = quantity; // آیتم جدید اضافه می‌کنیم
    }

    // ذخیره کوکی جدید
    setCookie(cookieName, JSON.stringify(menuData), 7); // 7 روز اعتبار
    console.log("Updated Cookie:", menuData);
}

// 4. حذف کوکی
function deleteCookie(name) {
    document.cookie = name + "=; Max-Age=0; path=/;";
    console.log("Cookie deleted:", name);
}

// مثال استفاده:
// روی کلیک آیتم
document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', function () {
        const itemName = this.getAttribute('data-name'); // نام آیتم از attribute
        const quantity = parseInt(this.getAttribute('data-quantity')); // تعداد آیتم
        updateCookie(itemName, quantity); // آپدیت کوکی
    });
});

// دکمه حذف کوکی
document.getElementById('deleteCookieButton').addEventListener('click', function () {
    deleteCookie("menuItems");
});