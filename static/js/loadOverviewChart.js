const loadOverviewChart = (chartData) => {
    var options = {
        series: chartData.datasets[0].data,
        labels: chartData.labels,
        chart: {
            type: 'pie',
            height: 350
        },
        title: {
            text: "Overview: Income vs. Expenses",
            align: 'center'
        },
        colors: ['#78e86c', "#e86363"],
    };

    var chart = new ApexCharts(document.querySelector("#overview-chart"), options);
    chart.render();
}
