
    // Get cart from cookies
    function test(){
        console.log("salam")
    }

    function getCookienn() {
        const cookies = document.cookie.split('; '); // Split cookies into key-value pairs
        const cookieDict = {};
        for (let cookie of cookies) {
            const [key, value] = cookie.split('=')
            cookieDict[key] = decodeURIComponent(value);
        }
        return cookieDict; 
}

    function setItemInCartnn(item_name, quantity) {
    // Get the existing cart from cookies (if any)
    console.log(item_name)
    const cartCookie = getCookie();
    // Parse the cart or initialize as an empty object
    
    // Update or add the item in the cart
    cartCookie[item_name] = quantity;
    //deletecartCookie('cart');
    console.log(cartCookie)
    
    // Save the updated cart back to the cookie
    //const expiration = new Date();
    //expiration.setTime(expiration.getTime() + 7 * 24 * 60 * 60 * 1000); // 7 days in milliseconds
    //document.cookie = `cart=${encodeURIComponent(JSON.stringify(cart))}; path=/; expires=${expiration.toUTCString()}`;
}
    // Save cart to cookies
    function deletecartCookie(name) {
    document.cookie= name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
}

    function setItemInCart(item_name, quantity) {
    console.log(`Adding to cart: ${item_name} (Quantity: ${quantity})`);

    // دریافت کوکی فعلی و تبدیل آن به آبجکت
    let cartCookie = getCookie()['cart'];  
    cartCookie = cartCookie ? JSON.parse(cartCookie) : {};  

    // بروزرسانی مقدار کوکی
    cartCookie[item_name] = quantity;

    // تبدیل آبجکت به رشته JSON و ذخیره در کوکی
    document.cookie = `cart=${encodeURIComponent(JSON.stringify(cartCookie))}; path=/; max-age=604800`; // 7 روز اعتبار

    console.log("Updated Cart:", cartCookie);
}
----------------------------------------------------------
function getCookie() {
    const cookies = document.cookie.split('; ');
    const cookieDict = {};
    for (let cookie of cookies) {
        const [key, value] = cookie.split('=');
        cookieDict[key] = decodeURIComponent(value);
    }
    return cookieDict;
}
