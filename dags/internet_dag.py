import speedtest
speed = speedtest.Speedtest()


def main():
    print('Counting...')
    print(f"Download speed: {'{:.2f}'.format(speed.download()/1024/1024)} Mb/s")
    print('Counting...')
    print(f"Upload speed: {'{:.2f}'.format(speed.upload()/1024/1024)} Mb/s")
    print('Exiting the program')
    return


if __name__ == '__main__':
    main()
