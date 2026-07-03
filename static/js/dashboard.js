const salesChart = document.getElementById("salesChart");
const orderChart = document.getElementById("orderStatusChart");

new Chart(salesChart, {
    type: "line",
    data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [{
            label: "Sales",
            data: [500, 1200, 1800, 2500, 3200, 2800],
            borderColor: "#4F46E5",
            backgroundColor: "rgba(79,70,229,0.15)",
            fill: true,
            tension: 0.6
        }]
    }
});

new Chart(orderChart,{
    type:"doughnut",
    data:{
        labels:["Pending", "Processing", "Delivered", "Cancelled"],
        datasets:[{
            data:[15, 30, 45, 10]
        }]
    }
});