from ytclass import ytDownloader
from data import data_handler
# Main program to use the ytDownloader class
def main():
    data_handler_obj = data_handler()
    # data_handler_obj.display_data()

    while True:
        print("\nYouTube Downloader Menu:")
        print("================================")
        print("1. Display Downloaded YouTube Data")
        print("2. Download Video")
        print("3. Download Audio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            print("*"*33,"\nDisplaying downloaded YouTube data:","\n","*"*33)
            data_handler_obj.display_data()
            print()
            
        elif choice == '2':
            print()
            print("*"*33,"\n Downloading Video","\n","*"*33)
            link = input("Enter the YouTube link for video download: ")
            downloader = ytDownloader(link)
            downloader.display_info()
            downloader.download_video('D:\Python\Projects\YTdownloader\YTfolder')
            print("Video downloaded successfully.")
            data_handler_obj.save_data({"Title":downloader.get_title(), "Views":downloader.get_views()})
            print()

        elif choice == '3':
            print()
            print("*"*33,"\n Downloading Audio","\n","*"*33)
            link = input("Enter the YouTube link for audio download: ")
            downloader = ytDownloader(link)
            downloader.display_info()
            downloader.download_audio('D:\Python\Projects\YTdownloader\YTaudio')
            print("Audio downloaded successfully.")
            data_handler_obj.save_data({"Title":downloader.get_title(), "Views":downloader.get_views()})
            print()

        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

