Run in this format:
<br />downloader.py
<br />decoder.py (optional, for mp3 files)
<br />visualiser.py -> the output images should be like "out.png" (memory sensitive script)
Always use a scaler for MLP, it is very very very sensitive to that.


Git management:
Since the models are so large, you'll not be able to upload it do github directly.
You need to use: https://git-lfs.com/

- first install git-lfs on the system.
- Now in local repo, run `git lfs install`
- Since we want to keep the models locally, but add a pointer for cloud repo, we will use
`git config --local filter.lfs.smudge "git-lfs smudge --skip -- %f"`
- since our models are in binary files, run: `git lfs track "*.pkl"`
- Now, stage the git attributes file: `git add .gitattributes`
- Since this repo was created long before lfs was added, we will use `git lfs migrate` to
also track previous commits.
