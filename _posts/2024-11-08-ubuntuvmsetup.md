---
layout: post
title: "SETTING UP AN UBUNTU DESKTOP VM"
author: Sal
categories: [Networking, post]
tags: [vm]
image: assets/images/UbuntuDesktop-Interface.png
---
**REQUIREMENT**
* VirtualBox 
* Ubuntu Desktop VM. Download the Ubuntu Desktop VM iso from the official Ubuntu [website](https://ubuntu.com/download/desktop).

### SETTING UP UBUNTU DESKTOP VM
- Launch VirtualBox and click *NEW*
  ![Alt text](/assets/images/UbuntuDesktopInstall0.png)
- Fill in the requirements
  ![Alt text](/assets/images/UbuntuDesktopInstall1.png)
  - Enter a desired name. Here we used *UbuntuDesktop*
  - Select the Ubuntu Desktop image from the stored folder. Here it is in the Download Folder
  - Check Skip Unattended Installation
  - Click Next
- Memory Allocation
  ![Alt text](/assets/images/UbuntuDesktopInstall2.png)
  ![Alt text](/assets/images/UbuntuDesktopInstall3.png)
- Finalization
  ![Alt text](/assets/images/UbuntuDesktopInstall4.png)
  Confirm the setup and click *Finish* to complete the process.

  ### INSTALLING UBUNTU DESKTOP
  On your VirtualBox click on the Ubuntu Desktop VM and click *start* to begin the Ubuntu Desktop VM installation process.
  ![Start VM](/assets/images/UbuntuDesktopInstall5.png)

  - Select a preferred language and click **Next**
  ![Sart VM](/assets/images/ubuntu-installation1.png)

  - On the accessibility settings, Click **Next**
  ![Ubuntu Installation](/assets/images/ubuntu-installation2.png)
  
  - Select a preferred keyboard layout and click **Next**
  ![Ubuntu Installation](/assets/images/ubuntu-installation3.png)
  
  - Select **Use wired connection** and click **Next** This will enable access to the internet for all necessary downloads during the installation process.
  ![Ubuntu Installation](/assets/images/ubuntu-installation4.png)
  
  - Select **Install Ubuntu** and click **Next**
  ![Ubuntu Installation](/assets/images/ubuntu-installation5.png)

  - Select **Interactive Installation** and click **Next** This ensures you get instructions as needed during the installation process.
  ![Ubuntu installation](/assets/images/ubuntu-installation6.png)
  
  - Select **Default selection** and click **Next**
  ![Ubuntu Installation](/assets/images/ubuntu-installation7.png)
  
  - This step is optional but it's a good practice to install recommended software and click **Next**
  ![Select Ubuntu](/assets/images/ubuntu-installation8.png)

  - Select **Erase disk and install Ubuntu** and click **Next**
  ![Select Ubuntu](/assets/images/ubuntu-installation9.png)

  - Enter the required details as instructed and click **Next**  
  ![Select Ubuntu](/assets/images/ubuntu-installation10.png)

  - Select a timezone of your choice and click **Next**
  ![Select Ubuntu](/assets/images/ubuntu-installation11.png)

  - Review your setup and click **Install** to proceed with the installation. 
  ![Select Ubuntu](/assets/images/ubuntu-installation12.png)

  - Click **Restart now** to finalize the process.
  ![Select Ubuntu](/assets/images/ubuntu-installation13.png)

 **COMMON PROBLEMS/ERROR**
  - Ubuntu 24.04 is not starting completely
  - Ubuntu 24.04 is freezing or working slow.
    
 **Reason**
    Ubuntu 24.04 unlike other versions requires more memory to function correctly. <br>
    You'll need to increase the base memory more if the issue persists after using the one suggested in the above screenshot.
    
