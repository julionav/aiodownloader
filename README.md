# aiodownloader
Async file downloader.

aiodownloader is a tool for downloading files asynchronously.

## Example usage
```
import asyncio

import aiodownloader

async def main(loop):
    downloader = aiodownloader.Handler(loop)

    # Downloading a file
    await downloader.download(url_of_file)

    await downloader.download_bulk(list_of_url_of_files)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
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
