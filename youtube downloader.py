from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from pytube.exceptions import RegexMatchError

def main():
    # make window
    window = Tk()
    window.title("Youtube video downloader")
    window.resizable(width=False, height=False)
    x = int(window.winfo_screenwidth()/2 - 200)
    y = int(window.winfo_screenheight()/2 - 50)
    window.geometry(f"400x100+{x}+{y}")
    window.config(bg="#4ac9f7")
    icon = PhotoImage(file=r"F:\mohamed files\images\Youtube.png")
    window.iconphoto(True, icon)

    # tell the user where to put the url
    text = Label(
        window, text="Inter the video URL", font=("Arial", 15), width=36, bg="#4af784"
    )
    text.pack()

    url_entry = Entry(window, font=("Arial", 15), width=36)
    url_entry.pack()

    submit = Button(
        window,
        text="Choose quality",
        font=("Arial", 15),
        bg="blue",
        activebackground="blue",
        fg="white",
        activeforeground="white",
        width=36,
        height=12,
        command=lambda: choose_quality(url_entry),
    )
    submit.pack()

    window.mainloop()


def choose_quality(url_entry):
    url = url_entry.get()
    resolutions, videos = get_resolutions(url)
    if resolutions == None:
        return

    new_win = Toplevel()
    x = int(new_win.winfo_screenwidth()/2 - 200)
    y = int(new_win.winfo_screenheight()/2 - 50)  
    new_win.geometry(f"400x100+{x}+{y+20}")
    new_win.resizable(width=False, height=False)
    new_win.config(bg="#4ec0f5")
    # title
    title = Label(new_win, text="Choose video quality", font=("Arial", 15), width=36, bg="#4ec0f5")
    title.pack()

    tmp = []
    for resolution in resolutions:
        tmp.append(str(resolution) + "p")

    resolutions = tmp
    quality = StringVar()
    quality.set(resolutions[0])
    # ask for video quality
    quality_list = OptionMenu(new_win, quality, *resolutions)
    quality_list.config(bg="#0bdb65", activebackground="#0cf571", fg="white", activeforeground="white", highlightbackground="#4ec0f5")
    quality_list.pack()

    submit = Button(
        new_win,
        text="Download Video",
        font=("Arial", 15),
        bg="#32CD32",
        activebackground="#32CD32",
        fg="#fc4319",
        activeforeground="#fc4319",
        width=36,
        command=lambda : download(videos, quality),
    )
    submit.pack()


def get_resolutions(url):
    # get video resolution
    resolutions = set()
    try:
        video = YouTube(url)
    except RegexMatchError:
        messagebox.showerror("url error", "Invalid URL!")
        return None 
    videos = video.streams.filter(type="video")
    for video in videos:
        resolutions.add(int((video.resolution).removesuffix("p")))
    return sorted(list(resolutions)), videos


def download(videos, quality):
    resolution = quality.get()
    video = videos.filter(res=resolution).first()
    video.download(r"F:\mohamed files")
    messagebox.showinfo("success", "Successfully downloaded at path: F:\mohamed files")


if __name__ == "__main__":
    main()
