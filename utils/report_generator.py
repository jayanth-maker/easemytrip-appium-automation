from datetime import datetime


def generate_html_report(results, execution_time):

    report_file = "reports/test_report.html"

    with open(report_file, "w") as f:

        f.write("<html>")
        f.write("<head>")
        f.write("<title>Automation Test Report</title>")
        f.write("</head>")
        f.write("<body>")

        f.write("<h1>EaseMyTrip Automation Test Report</h1>")

        f.write(f"<p><b>Date:</b> {datetime.now()}</p>")
        f.write(f"<p><b>Total Execution Time:</b> {execution_time} seconds</p>")

        f.write("<table border='1' style='border-collapse:collapse'>")
        f.write("<tr><th>Test Case</th><th>Status</th></tr>")

        for test, status in results:
            color = "green" if status == "PASS" else "red"
            f.write(f"<tr><td>{test}</td><td style='color:{color}'>{status}</td></tr>")

        f.write("</table>")

        f.write("</body>")
        f.write("</html>")

    print(f"HTML Report Generated → {report_file}")
