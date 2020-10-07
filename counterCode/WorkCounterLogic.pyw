# Project author:
# MachnevEgor_https://vk.com/machnev_egor
# Contact in email:
# meb.official.com@gmail.com

# import of all necessary libraries
import turtle
import datetime

# user settings
start_number = 0  # you can change - starting number of boxed
unit_of_counter = 1  # you can change - number of assembled boxes per click
box_weight = 10  # you can change - average weight of one box
number_of_products = 10  # you can change - number of products in one box
number_of_boxes_in_container = 10  # you can change - number of boxes for one container

# design settings
x_resolution = 480  # you can change - X screen resolution
y_resolution = 320  # you can change - Y screen resolution
background_color = "#2e2e2e"  # you can change - major color
main_color = "#888"  # you can change - line color
text_font = "Arial"  # you can change - font of text
big_font_size = 100  # you can change - big size of text
lateral_correction = 1.8  # you can change - lateral correction for side symbol
medium_font_size = 12  # you can change - medium size of text

# canvas creation
rootWindow = turtle.Screen()  # create screen
rootWindow.title("PackerOfGoods-WorkCounter")  # name of screen
rootWindow.setup(width=x_resolution, height=y_resolution)  # size of screen
rootWindow.bgcolor(background_color)  # background color

# creation edging
programFrame = turtle.Turtle(visible=False)  # create frame
programFrame.pensize(7)  # set settings for lines of frame
programFrame.pencolor(main_color)
programFrame.speed(0)
programFrame.penup()  # raise brush
programFrame.goto(0, (y_resolution / 2))  # set start point for drawing
programFrame.pendown()  # lower brush
programFrame.goto((x_resolution / 2), (y_resolution / 2))  # drawing field borders
programFrame.goto((x_resolution / 2), -(y_resolution / 2))
programFrame.goto(-(x_resolution / 2), -(y_resolution / 2))
programFrame.goto(-(x_resolution / 2), (y_resolution / 2))
programFrame.goto(0, (y_resolution / 2))  # moving to starting point

# bar creation
programFrame.penup()  # raise brush
programFrame.goto(-(x_resolution / 2), -(y_resolution / 2))  # set start point for drawing
programFrame.pendown()  # lower
for i in range(medium_font_size * 2 - round(lateral_correction)):  # filing
    programFrame.goto((x_resolution / 2), -((y_resolution / 2) - i))
    programFrame.goto(-(x_resolution / 2), -((y_resolution / 2) - i))

# creating a dividing line
programFrame.penup()  # raise brush
programFrame.goto(-(x_resolution / 2), (y_resolution / 2))  # set start point for drawing
programFrame.pendown()  # lower
for i in range(((x_resolution // 2) - (x_resolution // 2 // 3)) // 7 + (7 // 3)):  # filing
    programFrame.goto(-((x_resolution / 2) - (i * 7)), (y_resolution / 2))
    programFrame.goto(-((x_resolution / 2) - (i * 7)), -(y_resolution / 2))

# opening a file and then checking the settings fpr reading and writing
data_memory = open("dataSave.txt", "r+")  # import last save data
lines_list = list(data_memory.readlines())  # reading all lines from a text document
if len(lines_list) == 0:  # full erasure protection
    data_memory.write(
        "# Project author:" + "\n" + "# MachnevEgor_https://vk.com/machnev_egor" + "\n" + "# Contact in email:" + "\n" + "# meb.official.com@gmail.com")
if len(lines_list) <= 4:  # start of data recording, if there was clearing before
    now_date_and_time = datetime.datetime.today()  # current date and time
    data_memory.write(
        "\n" + "Production time and number of finished pieces:" + "\n" + str(now_date_and_time) + "\n" + str(
            start_number))
    work_counter = start_number
else:
    work_counter = int(lines_list[len(lines_list) - 1])  # other cases when everything is fine

# creation of the main counter
text_work_counter = (text_font, big_font_size)  # settings for design of text
object_work_counter = turtle.Turtle(visible=False)  # create object of counter
object_work_counter.color(main_color)
object_work_counter.penup()
object_work_counter.setposition((x_resolution / 2 / 3), -(big_font_size / 2))
object_work_counter.write(work_counter, align='center', font=text_work_counter)  # initial data output

# creation of an object of all output data
medium_text_settings = (text_font, medium_font_size)  # settings for design of text
quantity_left_side_lines = 0
# 1) creating title
quantity_left_side_lines += 1
object_title = turtle.Turtle(visible=False)  # create object of counter
object_title.color(background_color)
object_title.penup()
object_title.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_title.write("Product information:", align='left', font=medium_text_settings)  # initial data output

# 2.1) creating containers counter - word
quantity_left_side_lines += 2
object_number_of_containers_word = turtle.Turtle(visible=False)  # create object of counter
object_number_of_containers_word.color(background_color)
object_number_of_containers_word.penup()
object_number_of_containers_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_containers_word.write("--Number of containers:", align='left',
                                       font=medium_text_settings)  # initial data output

# 2.2) creating containers counter - number
quantity_left_side_lines += 1.5
object_number_of_containers = turtle.Turtle(visible=False)  # create object of counter
object_number_of_containers.color(background_color)
object_number_of_containers.penup()
object_number_of_containers.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_containers.write((work_counter // number_of_boxes_in_container), align='center',
                                  font=medium_text_settings)  # initial data output

# 2.3) creating containers counter of weight - word
quantity_left_side_lines += 1.5
object_weight_of_containers_word = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_containers_word.color(background_color)
object_weight_of_containers_word.penup()
object_weight_of_containers_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_containers_word.write("--Weight of container:", align='left',
                                       font=medium_text_settings)  # initial data output

# 2.4) creating containers counter of weight - number
quantity_left_side_lines += 1.5
object_weight_of_containers = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_containers.color(background_color)
object_weight_of_containers.penup()
object_weight_of_containers.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_containers.write(round((number_of_boxes_in_container * box_weight), 1), align='center',
                                  font=medium_text_settings)  # initial data output

# 3.1) creating boxes counter - word
quantity_left_side_lines += 2
object_number_of_boxes_word = turtle.Turtle(visible=False)  # create object of counter
object_number_of_boxes_word.color(background_color)
object_number_of_boxes_word.penup()
object_number_of_boxes_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_boxes_word.write("--Number of boxes:", align='left', font=medium_text_settings)  # initial data output

# 3.2) creating boxes counter - number
quantity_left_side_lines += 1.5
object_number_of_boxes = turtle.Turtle(visible=False)  # create object of counter
object_number_of_boxes.color(background_color)
object_number_of_boxes.penup()
object_number_of_boxes.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_boxes.write(work_counter, align='center', font=medium_text_settings)  # initial data output

# 3.3) creating boxes counter of weight - word
quantity_left_side_lines += 1.5
object_weight_of_boxes_word = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_boxes_word.color(background_color)
object_weight_of_boxes_word.penup()
object_weight_of_boxes_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_boxes_word.write("--Weight of box:", align='left', font=medium_text_settings)  # initial data output

# 3.4) creating boxes counter of weight - number
quantity_left_side_lines += 1.5
object_weight_of_boxes = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_boxes.color(background_color)
object_weight_of_boxes.penup()
object_weight_of_boxes.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_boxes.write(round(box_weight, 1), align='center', font=medium_text_settings)  # initial data output

# 4.1) creating boxes counter - word
quantity_left_side_lines += 2
object_number_of_goods_word = turtle.Turtle(visible=False)  # create object of counter
object_number_of_goods_word.color(background_color)
object_number_of_goods_word.penup()
object_number_of_goods_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_goods_word.write("--Number of products:", align='left',
                                  font=medium_text_settings)  # initial data output

# 4.2) creating boxes counter - number
quantity_left_side_lines += 1.5
object_number_of_goods = turtle.Turtle(visible=False)  # create object of counter
object_number_of_goods.color(background_color)
object_number_of_goods.penup()
object_number_of_goods.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_number_of_goods.write((work_counter * number_of_products), align='center',
                             font=medium_text_settings)  # initial data output

# 4.3) creating boxes counter of weight - word
quantity_left_side_lines += 1.5
object_weight_of_goods_word = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_goods_word.color(background_color)
object_weight_of_goods_word.penup()
object_weight_of_goods_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_goods_word.write("--Weight of product:", align='left',
                                  font=medium_text_settings)  # initial data output

# 4.4) creating boxes counter of weight - number
quantity_left_side_lines += 1.5
object_weight_of_goods = turtle.Turtle(visible=False)  # create object of counter
object_weight_of_goods.color(background_color)
object_weight_of_goods.penup()
object_weight_of_goods.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_weight_of_goods.write(round((box_weight / number_of_products), 1), align='center',
                             font=medium_text_settings)  # initial data output

# 5.1) creating total counter of weight - word
quantity_left_side_lines += 2
object_total_of_weight_word = turtle.Turtle(visible=False)  # create object of counter
object_total_of_weight_word.color(background_color)
object_total_of_weight_word.penup()
object_total_of_weight_word.setposition(-((x_resolution / 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_total_of_weight_word.write("Total weight:", align='left', font=medium_text_settings)  # initial data output

# 5.2) creating total counter of weight - number
quantity_left_side_lines += 1.5
object_total_of_weight = turtle.Turtle(visible=False)  # create object of counter
object_total_of_weight.color(background_color)
object_total_of_weight.penup()
object_total_of_weight.setposition(-((x_resolution / 2 / 3 * 2) - (medium_font_size / lateral_correction - 0.2)), (
(y_resolution / 2) - (medium_font_size * quantity_left_side_lines) - (medium_font_size / lateral_correction)))
object_total_of_weight.write(round((work_counter * box_weight), 1), align='center',
                             font=medium_text_settings)  # initial data output

# creation of an object of processing bar
object_processing = turtle.Turtle(visible=False)  # create object of counter
object_processing.color(background_color)
object_processing.penup()
object_processing.setposition(-(x_resolution / 2 - medium_font_size / (lateral_correction - 0.2)),
                              -(y_resolution / 2 - medium_font_size / lateral_correction))
object_processing.write("Ready", align='left', font=medium_text_settings)  # notification

# creation of an object of authorship
object_authorship = turtle.Turtle(visible=False)  # create object of counter
object_authorship.color(background_color)
object_authorship.penup()
object_authorship.setposition((x_resolution / 2 - medium_font_size / (lateral_correction - 0.2)),
                              -(y_resolution / 2 - medium_font_size / lateral_correction))
object_authorship.write("By: Machnev Egor", align='right', font=medium_text_settings)  # initial data output


def write_new_data(work_counter):  # writing new data in the database and updating data on the screen
    object_processing.clear()  # notification
    object_processing.write("Analysis and recording...", align='Left', font=medium_text_settings)
    object_number_of_containers.clear()  # redrawing
    object_number_of_containers.write((work_counter // number_of_boxes_in_container), align='right',
                                      font=medium_text_settings)
    object_number_of_boxes.clear()  # redrawing
    object_number_of_boxes.write(work_counter, align='center', font=medium_text_settings)
    object_number_of_goods.clear()  # redrawing
    object_number_of_goods.write((work_counter * number_of_products), align='center', font=medium_text_settings)
    object_total_of_weight.clear()  # redrawing
    object_total_of_weight.write(round((work_counter * box_weight), 1), align='center', font=medium_text_settings)
    now_date_and_time = datetime.datetime.today()  # import now date and time
    data_memory.write(
        "\n" + "Production time and number of finished pieces:" + "\n" + str(now_date_and_time) + "\n" + str(
            work_counter))
    object_processing.clear()  # notification
    object_processing.write("Ready", align='Left', font=medium_text_settings)


def up_work_counter():  # increasing the value
    object_processing.clear()  # notification
    object_processing.write("Add box", align='Left', font=medium_text_settings)
    global work_counter
    work_counter += unit_of_counter
    write_new_data(work_counter)
    object_work_counter.clear()
    object_work_counter.write(work_counter, align='center', font=text_work_counter)


def down_work_counter():  # decrease the value
    object_processing.clear()  # notification
    object_processing.write("Take away the box", align='Left', font=medium_text_settings)
    global work_counter
    if work_counter >= unit_of_counter:
        work_counter -= unit_of_counter
        write_new_data(work_counter)
        object_work_counter.clear()
        object_work_counter.write(work_counter, align='center', font=text_work_counter)
    else:
        object_processing.clear()  # notification
        object_processing.write("Value is minimum!", align='Left', font=medium_text_settings)
        object_processing.clear()  # notification
        object_processing.write("Ready", align='Left', font=medium_text_settings)


def reset_counter():  # reset the current value to the start
    object_processing.clear()  # notification
    object_processing.write("Reset value", align='Left', font=medium_text_settings)
    global work_counter
    work_counter = start_number
    write_new_data(work_counter)
    object_work_counter.clear()
    object_work_counter.write(work_counter, align='center', font=text_work_counter)


def delete_all_data():  # deleting all data from the database
    object_processing.clear()  # notification
    object_processing.write("Erase database...", align='Left', font=medium_text_settings)
    data_memory.truncate(0)  # delete all data
    data_memory.seek(0)  # moving cursor to the start of database
    data_memory.write(
        "# Project author:" + "\n" + "# MachnevEgor_https://vk.com/machnev_egor" + "\n" + "# Contact in email:" + "\n" + "# meb.official.com@gmail.com")
    object_processing.clear()  # notification
    object_processing.write("Ready", align='Left', font=medium_text_settings)


def redraw_counter():  # redraw output value
    object_processing.clear()  # notification
    object_processing.write("Redraw value", align='Left', font=medium_text_settings)
    object_work_counter.clear()  # redrawing
    object_work_counter.write(work_counter, align='center', font=text_work_counter)
    object_number_of_containers.clear()  # redrawing
    object_number_of_containers.write((work_counter // number_of_boxes_in_container), align='right',
                                      font=medium_text_settings)
    object_number_of_boxes.clear()  # redrawing
    object_number_of_boxes.write(work_counter, align='center', font=medium_text_settings)
    object_number_of_goods.clear()  # redrawing
    object_number_of_goods.write((work_counter * number_of_products), align='center', font=medium_text_settings)
    object_total_of_weight.clear()  # redrawing
    object_total_of_weight.write(round((work_counter * box_weight), 1), align='center', font=medium_text_settings)
    object_processing.clear()  # notification
    object_processing.write("Ready", align='Left', font=medium_text_settings)


# reading keys to trigger actions
rootWindow.listen()  # reading keystrokes
rootWindow.onkeypress(up_work_counter, "space")
rootWindow.onkeypress(down_work_counter, "z")
rootWindow.onkeypress(reset_counter, "r")
rootWindow.onkeypress(delete_all_data, "d")
rootWindow.onkeypress(redraw_counter, "Tab")

rootWindow.mainloop()

# Project author:
# MachnevEgor_https://vk.com/machnev_egor
# Contact in email:
# meb.official.com@gmail.com
