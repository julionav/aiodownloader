# aiodownloader
Async file downloader.

aiodownloader is a simple tool that allows to download files in parallel
without the overhead of using multiple processes by using instead the async
features of python.

## Example usage

### Using it in a synchronous program

```
import aiodownloader

def download_sync():
    downloader = aiodownloader.Handler() # Sync defaults to True

    # Downloading a file
    downloader.download(url_of_file)

    # Downloading multiple files
    await downloader.download(*list_of_url_of_files)


if __name__ == '__main__':
    download_sync()
```

### Using it in an async program.

```
import asyncio

import aiodownloader

async def downlaod_async():
    downloader = aiodownloader.Handler(sync=False)

    # Downloading a file
    await downloader.download(url_of_file)

    await downloader.download(*list_of_url_of_files)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_async())
```


## Features (whishlist)
- [x] Basic downloader
- [ ] The downloader can pause and continue downloads
- [ ] The downloader can be run in another thread so the users program doesn't have to use asyncio
- [ ] A cli for the downloader
- [ ] It can be daemonized
- [ ] The cli can interact with the daemon
- [ ] Downloads can be prioritized and schuedled
- [ ] Awesome UI made with electron.
- and many more...
