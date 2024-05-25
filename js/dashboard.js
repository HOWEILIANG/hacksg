document.addEventListener("DOMContentLoaded", function () {
  // Function to create doughnut chart for stock percentages
  function createStockPercentagesChart() {
    var ctx = document.getElementById("stockPercentagesChart").getContext("2d");
    var stockPercentagesChart = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: ["Stock A", "Stock B", "Stock C"],
        datasets: [
          {
            label: "Stock Percentages",
            data: [30, 40, 30], // Example data
            backgroundColor: [
              "rgba(255, 99, 132, 0.5)",
              "rgba(54, 162, 235, 0.5)",
              "rgba(255, 206, 86, 0.5)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  }

  // Function to create line chart for stock market rates
  function createStockMarketRatesChart() {
    var ctx = document.getElementById("stockMarketRatesChart").getContext("2d");
    var stockMarketRatesChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "Stock Market Rates",
            data: [150, 160, 170, 180, 190, 200], // Example data
            backgroundColor: "rgba(54, 162, 235, 0.5)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  }

  // Function to create line chart for returns
  function createReturnsChart() {
    var ctx = document.getElementById("returnsChart").getContext("2d");
    var returnsChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "Returns",
            data: [0.03, 0.05, 0.04, 0.06, 0.05, 0.07], // Example data
            backgroundColor: "rgba(255, 99, 132, 0.5)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  }

  // Function to create line chart for dividends
  function createDividendsChart() {
    var ctx = document.getElementById("dividendsChart").getContext("2d");
    var dividendsChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "Dividends",
            data: [2.5, 3, 2.8, 3.2, 3.5, 3.1], // Example data
            backgroundColor: "rgba(255, 206, 86, 0.5)",
            borderColor: "rgba(255, 206, 86, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      },
    });
  }

  // Call functions to create charts
  createStockPercentagesChart();
  createStockMarketRatesChart();
  createReturnsChart();
  createDividendsChart();
});
