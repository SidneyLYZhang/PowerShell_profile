# PowerShell Profile 

**From sidney zhang**

Last updated on 2019-10-18

This is my configuration files for PowerShell(5.1 and Core 6). In PowerShell this config-file called "profile.ps1".
Of course, this config-file is a powershell script. It's crazy, isn't it?

## Where are those Config-Files(profile)?

As simple :

```powershell
PS > $PROFILE

C:\Users\<user_name>\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
```

For all locations of those config-files :

```powershell
PS > $PROFILE | Format-List -Force

AllUsersAllHosts       : C:\Windows\System32\WindowsPowerShell\v1.0\profile.ps1
AllUsersCurrentHost    : C:\Windows\System32\WindowsPowerShell\v1.0\Microsoft.PowerShell_profile.ps1
CurrentUserAllHosts    : C:\Users\<user_name>\Documents\WindowsPowerShell\profile.ps1
CurrentUserCurrentHost : C:\Users\<user_name>\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
Length                 : 75

```

In [Microsoft official documentation](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6) , you can also find this information.

## Create a Config-File

First, you will ask, whether this config-file already exists. Two ways to confirm this question:

1. open this folder and find it. 
2. use a command line :

```powershell
PS > Test-Path -Path $PROFILE

True
```

If this output is "True", that means, this config-file is already existing. If not , you need to create one for powershell.

Second, how to create one config-file?

It's also too easy to reach the destination:

- Use notepad to create a new file, and save it as "profile.ps1" in that folder.
- Use another command line to automatically create one :

```powershell
PS > New-Item -Path $PROFILE -Name "profile.ps1" -ItemType "file" -Value "#profile..."

    目录: C:\Users\<user_name>\Documents\WindowsPowerShell


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----       2019/10/18     17:25             17 profile.ps1
```

After all, you will be able to edit this file to deploy your PowerShell on your preferences. Of course, you can use my favorite profile.

## Commission Your PowerShell

My favorite PowerShell View:

![](Assets/view.png)

You can get my profile :

```powershell
PS > git 
```

### Getting Started From Themas

******

## Reference

1. https://sspai.com/post/52907
2. https://sspai.com/post/52868
3. https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables?view=powershell-6
4. https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-6
5. https://coolcode.org/2018/03/16/how-to-make-your-powershell-beautiful/
6. https://zhuanlan.zhihu.com/p/51901035