# dpy-boilerplate

Opinionated boilerplate configurations for bots written in Python using [discord.py](https://github.com/Rapptz/discord.py).

This project contains 2 boilerplate repositories that you can use to kickstart your Discord bot project(s).

**NOTE:** Although you can use this for your first project, I highly recommend understanding every bit of code that is written before relying on it, if not trying to code on your own first. These templates are meant for returning devs who want to spin up a bot quickly without setting up the necessities.

## Choosing between basic and advanced

There are a bunch of distinctions between the 2 configs. The major ones are listed below!

| Feature                 | Basic              | Advanced           |
|-------------------------|:------------------:|:------------------:|
| Cog-based architecture  | :heavy_check_mark: | :heavy_check_mark: |
| Prefix command examples | :heavy_check_mark: | :heavy_check_mark: |
| Slash command examples  | :heavy_check_mark: | :heavy_check_mark: |
| Database                | SQLite             | PostgreSQL         |
| Logging                 | :x:                | :heavy_check_mark: |
| Client session          | :x:                | :heavy_check_mark: |
| Custom help command     | :x:                | :heavy_check_mark: |
| Dev environment         | :x:                | :heavy_check_mark: |

**TL;DR:** Basic is good for a small scale bot with limited features. Advanced has a lot more options that you'd need when having a bigger feature-set.

Note: If you want to set up basic but want a feature from advanced without its entirity, you can grab it from there with little extra config.

## Setup

The general setup for both the templates will look the same.

1. You get the repository cloned on your system
2. Set the initial configuration
3. Search and complete all the FIXMEs in the code. Optionally the TODOs as well.

<details>
<summary>Installation for basic</summary>

1. Clone the repository. Since we want to truncate the git history, let's get the latest zip. Replace `<new-repo-name>` with any name you like.
    ```sh
    curl -L https://git.sr.ht/~getpsyched/dpy-boilerplate-basic/archive/master.tar.gz | gunzip | tar xv
    mv dpy-boilerplate-basic-master <new-repo-name>
    cd <new-repo-name> && git init
    ```

2. Set the environment variables in the `.env`.

3. Done! Simply eliminate the FIXMEs and TODOs and you're setup with a nice little bot repo.
</details>

<details>
<summary>Installation for advanced</summary>

Skip local setup and deploy as is while forking this repo:
<br>
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/vdTx0A?referralCode=5miY8S)

1. Clone the repository. Since we want to truncate the git history, let's get the latest zip. Replace `<new-repo-name>` with any name you like.
    ```sh
    curl -L https://git.sr.ht/~getpsyched/dpy-boilerplate-advanced/archive/master.tar.gz | gunzip | tar xv
    mv dpy-boilerplate-basic-master <new-repo-name>
    cd <new-repo-name> && git init
    ```

2. Set the environment variables in the `.env`.

3. TODO
</details>
