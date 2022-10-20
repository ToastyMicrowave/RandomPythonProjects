from ast import Break
import pyperclip 
import pyautogui as pag
import webbrowser
import PIL
import time
sub_name_list = []
no_flare_required_sub_list = []
title = "H0rny College Teacher loves to Suck and Stroke Diçks of her Students🥵 Don't Miss Full Video🤩❤️ [Link in Comments]"
thumbnail_link = "https://www.redgifs.com/watch/boilingtornpony"
video_link = "Full Video - https://droplink.co/H0rnyIndianTeacher"
flair_button_png = r"C:\Users\kapil\Pictures\Screenshot 2022-07-28 155215.png"
post_button_png = r"C:\Users\kapil\Pictures\Screenshot 2022-07-28 154821.png"
comment_area_png = r"C:\Users\kapil\Pictures\Screenshot 2022-07-28 150452.png"
comment_button_png = r"C:\Users\kapil\Pictures\Screenshot 2022-07-26 203825.png"
with open("C:\Python Projects\lulw2.txt", "r") as sub_names_file:    # This is where the file containing the sub name list goes
    for x in sub_names_file.read().strip().split("\n"):
        sub_name_list.append(x)    # Creates list of all the subreddit names 
with open(r"C:\Python Projects\no flair needed.txt", "r") as no_flair_required_sub_names_file:    # This is where the file containing the no flair needed sub name list goes
    for y in no_flair_required_sub_names_file.read().strip().split("\n"):
        no_flare_required_sub_list.append(y)    # Creates list of all the subreddit names that dont need flairs before posting
for sub_name in sub_name_list:
    webbrowser.open("https://www.reddit.com/r/" + sub_name + "/submit" )    # This opens the subbredit in the default browser
    pag.sleep(7)
    pag.click(781, 299)    # Clicks on "Link" type of post
    pag.click(461, 363)    # Clicks on "Title" area
    if sub_name == "Desi4you" or "Sexyindianwives":
        pag.typewrite(title.removesuffix("[Link in Comments]"))
    elif sub_name == "HotDesiSluts":
        pag.typewrite((title.removesuffix(" Comments]")) + "Profile]")
    else:
        pag.typewrite(title)   # Types title into title area
    pag.click(452, 427)    # Clicks on "url" area
    pag.typewrite(thumbnail_link)    # Types the link into url area
    pag.sleep(2)
    if sub_name not in no_flare_required_sub_list:
        coords_of_flair_button = pag.locateCenterOnScreen(flair_button_png, confidence = 0.8)    # Finds coords of flair button
        if coords_of_flair_button != None:
            pag.click(coords_of_flair_button)    # Clicks on flair button
            pag.click(856, 465)    # Clicks on flair search area
            if sub_name == "Desi4you":
                pag.typewrite("nsfw")
            elif sub_name == "IndianCelebScenes":
                pag.typewrite("new")
            elif sub_name == "SuperModelIndia":
                pag.typewrite("misc")
            elif sub_name == "UnratedPanda":
                pag.typewrite("amateur porn")
            else:
                pag.typewrite("link")    # Types "link" in the search area
            pag.click(776, 515)    # Clicks on the first flair after searching
            pag.click(1088, 835)    # Clicks on apply flair
            pag.sleep(2)
        else:
            print("No flair button found in the {} post screen".format(sub_name))
            continue
    coords_of_post_button = pag.locateCenterOnScreen(post_button_png, confidence = 0.8)    # Finds coords of post button
    if coords_of_post_button != None:
        pag.click(coords_of_post_button)    # Moves to the "post button"
    else:
        print("No post button found in the {} post screen".format(sub_name))
        continue
    pag.sleep(5)
    pag.scroll(-500)    # Scrolls a little so that the comment area is on screen
    comment_area_coords = pag.locateCenterOnScreen(comment_area_png, confidence = 0.9)    # Finds coords of the comment area
    if comment_area_coords != None:
        pag.click(comment_area_coords)    # Clicks on comment area
    else:
        print(("No comment area found in the {} post's comment screen".format(sub_name)))
        continue
    pyperclip.copy(video_link)    # Copies video download link
    pag.hotkey("ctrl", "v")    # Pastes the video link
    pag.sleep(1)
    comment_button_coords = pag.locateCenterOnScreen(comment_button_png, confidence = 0.8)    # Finds coords of comment button
    if comment_button_coords != None:
        pag.click(comment_button_coords)    # Clicks on comment button
    else:
        print("No comment button found in the {} post's comment screen".format(sub_name))
        continue
    pag.sleep(2)
    pag.hotkey("ctrl", "w")    
    pag.press("enter")
    
    
   