/** 
$(document).ready(function () {
  function createStockProportionChart() {
    var ctx = $("#stockProportionChart");
    var stockProportionChart = new Chart(ctx, {
      type: "pie",
      data: {
        labels: ["Stock A", "Stock B", "Stock C"],
        datasets: [
          {
            label: "Stock Proportion",
            data: [30, 40, 30], // Sample data
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

  function createStockPerformanceChart() {
    var ctx = $("#stockPerformanceChart");
    var stockPerformanceChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "Stock Performance",
            data: [100, 120, 110, 130, 125, 140], // Sample data
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

  function createDividendYieldTrendChart() {
    var ctx = $("#dividendYieldTrendChart");
    var dividendYieldTrendChart = new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["2019", "2020", "2021", "2022", "2023", "2024"],
        datasets: [
          {
            label: "Dividend Yield Trend",
            data: [5, 6, 7, 6, 8, 7], // Sample data
            backgroundColor: "rgba(255, 206, 86, 0.5)",
            borderColor: "rgba(255, 206, 86, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  }

  function populateSelectedStockData() {
    var selectedStockData = $("#selectedStockData");
    var data = [
      { stock: "Stock A", price: "$100", change: "+2.5%" },
      { stock: "Stock B", price: "$120", change: "-1.2%" },
      { stock: "Stock C", price: "$90", change: "+3.8%" },
    ];
    var table =
      '<table class="table"><thead><tr><th>Stock</th><th>Price</th><th>Change</th></tr></thead><tbody>';
    $.each(data, function (index, item) {
      table +=
        "<tr><td>" +
        item.stock +
        "</td><td>" +
        item.price +
        "</td><td>" +
        item.change +
        "</td></tr>";
    });
    table += "</tbody></table>";
    selectedStockData.html(table);
  }

  createStockProportionChart();
  createStockPerformanceChart();
  createDividendYieldTrendChart();
  populateSelectedStockData();
});
*/

$(document).ready(function () {
  // Fetch data from Django backend
  $.ajax({
    url: "/path/to/your/django/view",
    method: "GET",
    success: function (data) {
      // Parse the data (assuming it's JSON)
      var parsedData = JSON.parse(data);

      // Use the data to update your charts
      updateStockProportionChart(parsedData.stockProportionData);
      updateSelectedStockData(parsedData.selectedStockData);
      updateStockPerformanceChart(parsedData.stockPerformanceData);
      updateDividendYieldTrendChart(parsedData.dividendYieldTrendData);
    },
    error: function (error) {
      console.log("Error:", error);
    },
  });

  // Placeholder functions for updating your charts
  function updateStockProportionChart(data) {
    // Update your Stock Proportion chart with the provided data
  }

  function updateSelectedStockData(data) {
    // Update your Selected Stock Data with the provided data
  }

  function updateStockPerformanceChart(data) {
    // Update your Stock Performance chart with the provided data
  }

  function updateDividendYieldTrendChart(data) {
    // Update your Dividend Yield Trend chart with the provided data
  }
});
