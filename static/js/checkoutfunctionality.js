// checkout section
const payButton = document.getElementById("pay-button");

if (payButton) {

    const options = {
        key: payButton.dataset.key,

        amount: payButton.dataset.amount,

        currency: payButton.dataset.currency,

        name: "Your Store",

        description: `Order #${payButton.dataset.orderNumber}`,

        order_id: payButton.dataset.orderId,

        handler: function (response) {
            console.log("Payment successful");
            console.log("Payment ID:", response.razorpay_payment_id);
            console.log("Order ID:", response.razorpay_order_id);
            console.log("Signature:", response.razorpay_signature);

    alert("Payment successful!");
            // window.location.href = `/orders/payment-success/${response.razorpay_order_id}/`;
        },
        
        theme: {
            color: "#4f46e5"
        }
    };

    const razorpay = new Razorpay(options);
    
    payButton.onclick = function(e) {

        e.preventDefault();

        razorpay.open();

    };

}