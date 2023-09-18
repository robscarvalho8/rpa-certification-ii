# Template: Python - Minimal

This template leverages the new Python open-source structure [robo](https://github.com/robocorp/robo), the [libraries](https://github.com/robocorp/robo#libraries) from to same project as well.
The full power of [rpaframework](https://github.com/robocorp/rpaframework) is also available for you on Python as a backup while we implement new Python libraries.

The template provides you with the basic structure of a Python project: logging out of the box and controlling your tasks without fiddling with the base Python stuff. The environment contains the most used libraries, so you do not have to start thinking about those right away.

👉 After running the bot, check out the `log.html` under the `output` -folder.

The template here is essentially empty, leaving you with a canvas to paint on.

Do note that with Robocorp tooling you:
- Do NOT need Python installed
- Should NOT be writing `pip install..`; the [conda.yaml](https://github.com/robocorp/template-python/blob/master/conda.yaml) is here for a reason.
- You do not need to worry about Python's main -functions and, most importantly, the logging setup

🚀 Now, go get'em

For more information, do not forget to check out the following:
* [Robocorp Documentation -site](https://robocorp.com/docs)
* [Portal for more examples](https://robocorp.com/portal)
* [robo repo](https://github.com/robocorp/robo) as this will developed a lot...

## Rules

- URL: https://robotsparebinindustries.com/#/robot-order
- The robot should use the [orders file](https://robotsparebinindustries.com/orders.csv) (.csv ) and complete all the orders in the file.
- Only the robot is allowed to get the orders file. You may not save the file manually on your computer.
- The robot should save each order HTML receipt as a PDF file.
- The robot should save a screenshot of each of the ordered robots.
- The robot should embed the screenshot of the robot to the PDF receipt.
- The robot should create a ZIP archive of the PDF receipts (one zip archive that contains all the PDF files). Store the archive in the output directory.
- The robot should complete all the orders even when there are technical failures with the robot order website.
- The robot should be available in public GitHub repository.
- It should be possible to get the robot from the public GitHub repository and run it without manual setup.