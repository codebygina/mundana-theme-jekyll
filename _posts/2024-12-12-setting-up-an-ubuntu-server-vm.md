---
layout: post
title: "SETTING UP AN UBUNTU SERVER VM"
author: Snowdiamond
categories: [Jekyll, post]
tags: [vm]
image: assets/images/ubuntu-server-logo.jpeg
---
**REQUIREMENT**
* VirtualBox 
* Ubuntu Server Image. You can download the Ubuntu server iso from the official Ubuntu [website](https://ubuntu.com/download/server#manual-install).
  
**NOTE: WE ARE USING UBUNTU SERVER 22.04 FOR THIS INSTALLATION PROCESS.**
  
### SETTING UP UBUNTU DESKTOP VM
- Launch VirtualBox and click **NEW**
  ![Alt text](/assets/images/UbuntuDesktopInstall0.png)
- Fill in the requirements
  ![Alt text](/assets/images/ubuntu-server-setup-1.png)
  - Enter a desired name. Here we used **Ubuntu-server-gateway**
  - Select the Ubuntu Server image from the stored folder. Here it is in the Download Folder
  - Check Skip Unattended Installation
  - Click Next
- Memory Allocation
  ![Alt text](/assets/images/ubuntu-server-setup-2.png)
  ![Alt text](/assets/images/ubuntu-server-setup-3.png)
- Finalization
  ![Alt text](/assets/images/ubuntu-server-setup-4.png)
  Confirm the setup and click **Finish** to complete the process.

  ### INSTALLING UBUNTU SERVER
  On your VirtualBox click on the Ubuntu Server VM and click **start** to begin the Ubuntu Server installation process.
  ![Start VM](/assets/images/UbuntuDesktopInstall5.png)

  - Select the option to **try and install ubuntu server**
   ![Start VM](/assets/images/ubuntu-server-install-1.png)

  - Select a preferred language and press **Enter**
  ![Sart VM](/assets/images/ubuntu-server-install-2.png)

  - You have the option to continue without updating to a new installer or update to a new install, always use the update option except you have a need to use an older version like in this situation. Select the right option and press **ENTER** 
  ![Ubuntu Installation](/assets/images/ubuntu-server-install-3.png)
  
  - Select a preferred keyboard layout, navigate to **Done** and press **Enter** to proceed.
  ![Ubuntu Installation](/assets/images/ubuntu-server-install-4.png)
  
  - Select **ubuntu server** as the base for the installation. Select **Done** and press **Enter**
  ![Ubuntu Installation](/assets/images/ubuntu-server-install-5.png)

  - There are two options to proceed from this step. We can either configure the network interface from the terminal or proceed and do the configuration later. Here we'll proceed and configure it later. So, select **Done** and press **Enter** to proceed
  ![Ubuntu installation](/assets/images/ubuntu-server-install-6.png)
  
  - We do not require a proxy to continue this installation navigate to **Done** and press **Enter** to proceed
  ![Ubuntu Installation](/assets/images/ubuntu-server-install-7.png)
  
  - Check **use the entire disk and set up this disk as LVM group** then navigate to **Done** and press **Enter** to proceed. You have the option to encrypt your disk at this stage if you need an extra layer of security
  ![Select Ubuntu](/assets/images/ubuntu-server-install-9.png)

  - Review the setup then navigate to **Done** and press **Enter** to proceed
  ![Select Ubuntu](/assets/images/ubuntu-server-install-10.png)

  - When prompted, select **Continue** then press **Enter**  
  ![Select Ubuntu](/assets/images/ubuntu-server-install-11.png)

  - Fill in the required information, navigate to **Done** and press **Enter** to proceed
  ![Select Ubuntu](/assets/images/ubuntu-server-install-12.png)

  - The upgrade step is optional. We are skipping it for this installation. Navigate to **Continue** and press **Enter** to proceed with the installation.
  ![Select Ubuntu](/assets/images/ubuntu-server-install-13.png)

  - Check **Install openSSH server** to be able to use SSH when needed. Navigate to **Done** Press **Enter** to proceed.
  ![Select Ubuntu](/assets/images/ubuntu-server-install-14.png)
  
  - Check the needed service. This depends on the intended use of the server. Navigate to **Done** and Press **Enter** to proceed.
  ![Select Ubuntu](/assets/images/ubuntu-server-install-15.png)

  - Select **Reboot now** and press **Enter** to finalise the installation.
  ![Select Ubuntu](/assets/images/ubuntu-server-install-16.png)
 
  - Manually unmount the virtual disk (Click on Devices> optical drive to do so) if the automatic unmounting process fails.

  - Enter the username and password when prompted to login.
  ![Select Ubuntu](/assets/images/ubuntu-server-install-17.png)
  
 **COMMON PROBLEMS/ERROR**
  - Not selecting the needed services during installation.
