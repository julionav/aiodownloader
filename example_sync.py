"""
Example usage for the downloader in async mode. It shows how to download a single and 
multiple files file with the downloader
"""
import logging

import aiodownloader

logging.basicConfig(level='DEBUG')


def download_sync():
    downloader = aiodownloader.Handler(sync=True)

    # Downloading a file
    downloader.download('https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif')

    downloader.download(*[
        'https://www.visualstudio.com/wp-content/uploads/2016/06/python-1-562x309@2x-op.png',
        'https://media.giphy.com/media/Vuw9m5wXviFIQ/giphy.gif',
        'https://cdn-images-1.medium.com/max/800/1*6V7WZZ5rhCWJvRzevnAh5g.png',
    ])


if __name__ == '__main__':
    download_sync()
