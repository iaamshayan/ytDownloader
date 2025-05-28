# 🎬 YouTube Downloader Console App (Practice Project)

Welcome to my simple **YouTube Downloader** project, created as part of my **Python learning journey**! This is a basic console application written in Python that allows users to:

- 🎥 Download YouTube videos
- 🎵 Extract audio from YouTube videos
- 📄 Save and display video metadata (title and views)

I plan to **iteratively enhance** this tool as I learn more advanced Python concepts, libraries, and techniques.

---

## ✅ Features Implemented So Far

- 📥 **Video Download**: Input a YouTube link and download the video in the highest available quality.
- 🔊 **Audio Download**: Download only the audio from a YouTube video as MP3.
- 📂 **Data Saving**: Store downloaded video info (title and views) in a JSON file.
- 📃 **Data Display**: View all saved YouTube video metadata in a readable format.
- ❌ **Basic Error Handling**: Handles invalid links and missing files gracefully.

---

## 📁 Project Structure

```
YTdownloader/
│
├── ytclass.py          # ytDownloader class using yt_dlp
├── data.py             # data_handler class for saving/loading JSON data
├── main.py             # Main menu-driven interface
├── yt_data.txt         # JSON file to store downloaded video data
└── README.md           # Project info and contribution guidelines
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Install the required library:
   ```
   pip install yt-dlp
   ```
3. Run the program:
   ```
   python main.py
   ```

---

## 📌 Notes

- This is a **practice project** to learn Python.
- Code will improve and evolve over time.
- Feedback, suggestions, and **pull requests are welcome**!

---

## 🚀 Future Plans

- [ ] Add video/audio format selection
- [ ] Add progress bars or status indicators
- [ ] Implement multithreading for faster downloads
- [ ] Build a GUI version using Tkinter or PyQt
- [ ] Add support for playlist downloads

---

## 🙌 Contributions

If you find bugs, have ideas, or just want to improve the project — **feel free to fork it, submit pull requests, or open issues**!

---

## 🧠 Author

Built by a Python learner who’s passionate about building real-world tools while leveling up skills. 💡

---

Thank you for checking this out! 🚀
```