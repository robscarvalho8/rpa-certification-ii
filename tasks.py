from robocorp import browser, http
from robocorp.tasks import task

from RPA.Archive import Archive
from RPA.PDF import PDF
from RPA.Tables import Tables


@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    browser.configure(slowmo=100)
    open_robot_order_website()
    orders = get_orders()
    for order in orders:
        fill_and_submit_orders_form(order)
        path_pdf = store_receipt_as_pdf(order["Order number"])
        page = browser.page()
        path_screenshot = screenshot_robot(order["Order number"])
        embed_screenshot_to_receipt(path_screenshot, path_pdf)

        page.click("#order-another")
    archive_receipts()


def open_robot_order_website():
    """Downloads excel file from the given URL"""
    browser.goto(url="https://robotsparebinindustries.com/#/robot-order")


def get_orders():
    """Downloads excel csv from the given URL"""
    http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)

    library = Tables()
    orders = library.read_table_from_csv("orders.csv", header=True, delimiters=",")
    return orders


def fill_and_submit_orders_form(orders_rep):
    """Fills in the orders data and click the 'Preview' button"""
    page = browser.page()
    page.click("text=OK")

    radio_buttons = {
        "1": "Roll-a-thor body",
        "2": "Peanut crusher body",
        "3": "D.A.V.E body",
        "4": "Andy Roid body",
        "5": "Spanner mate body",
        "6": "Drillbit 2000 body",
    }

    page.select_option("#head", orders_rep["Head"])
    page.click(f"text={radio_buttons.get(orders_rep['Body'])}")
    page.fill("input[type=number]", orders_rep["Legs"])
    page.fill("#address", orders_rep["Address"])
    page.click("#order")
    while get_errors():
        page.click("#order")


def get_errors():
    """Verify errors when sent order"""
    page = browser.page()
    try:
        page.locator(".alert").text_content()
        return True
    except:
        return False


def store_receipt_as_pdf(order_number):
    """Export the data to a pdf file"""
    page = browser.page()
    order_results_html = page.locator("#receipt").inner_html()
    path = f"pdf/order_{order_number}.pdf"
    pdf = PDF()
    pdf.html_to_pdf(order_results_html, path)
    return path


def screenshot_robot(order_number):
    """Export image from roboto data to a png file"""
    page = browser.page()
    image = page.locator("#robot-preview-image")
    path = f"screenshot/screenshot_order_{order_number}.png"
    image.screenshot(path=path)
    return path


def embed_screenshot_to_receipt(path_screenshot, path_pdf):
    """Embeds the screenshot to the receipt PDF."""
    pdf = PDF()
    pdf.add_files_to_pdf(
        files=[path_pdf, path_screenshot],
        target_document=path_pdf
        )


def archive_receipts():
    """Creates ZIP archive of the receipts and the images."""
    lib = Archive()
    lib.archive_folder_with_zip("pdf", "output/receipts.zip")