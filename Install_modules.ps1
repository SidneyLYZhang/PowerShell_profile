<#  ==============================================================================================================
     _              _           _  _                           _         _
    (_) _ __   ___ | |_   __ _ | || |    _ __ ___    ___    __| | _   _ | |  ___  ___
    | || '_ \ / __|| __| / _` || || |   | '_ ` _ \  / _ \  / _` || | | || | / _ \/ __|
    | || | | |\__ \| |_ | (_| || || |   | | | | | || (_) || (_| || |_| || ||  __/\__ \
    |_||_| |_||___/ \__| \__,_||_||_|   |_| |_| |_| \___/  \__,_| \__,_||_| \___||___/

    ==============================================================================================================  #>
# Update 2019-11-08
# Coding by sidneyzhang <zly@liangyi.me>

<#  ----------------------------------------------FIRST-SETTING---------------------------------------------------  #>

Write-Host "Starting to Setting Policies..."
Set-PSRepository -Name PSGallery -InstallationPolicy Trusted
Set-ExecutionPolicy -Scope CurrentUser Bypass

<#  --------------------------------------------------NORMAL------------------------------------------------------  #>

Write-Host "`nBeginning to Installing ..."
$packages = @("PSColor", "Get-ChildItemColor", "posh-git", "oh-my-posh", "windows-Screenfetch")
$n = 1
Write-Host "Starting to Setting Policies..."
foreach ($item in $packages) {
    Write-Host ("    " + $n + ": " + $item) -ForegroundColor ([enum]::GetValues([System.ConsoleColor]) | Get-Random)
    Install-Module -Name $item -Scope CurrentUser
    $n++
}

<#  --------------------------------------------------LOLCAT------------------------------------------------------  #>

Write-Host "`nTesting whether the command `"lolcat`" exists..."

function Test-CommandExist 
{
    param(
        [switch]
        [Alias("f")]
        $Full
    )
    begin {
        try{
            $tip = Get-Command -ErrorAction "Stop" $args
        }
        catch {
            $tip = ""
        }
    }
    process {
        if($tip -eq ""){
            $so = $False
        } else {
            $so = $True
        }
        $result = @{
            "Information" = $tip;
            "Result" = $so
        }
    }
    end {
        if ($Full){
            return $result
        } else {
            return $result.Result
        }
    }
}

$test_res = Test-CommandExist "lolcat"

if (-not $test_res) {
    $fl = "https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.6.5-1/rubyinstaller-devkit-2.6.5-1-x64.exe"
    $outfl = $HOME + "\Downloads\" + "rubyinstaller.exe"
    Write-Host "`"lolcat`" dos't exist...`nNow Install it..."
    Write-Host "Download the files ..."
    (New-Object System.Net.WebClient).DownloadFile($fl,$outfl)
    Start-Process $outfl
} else {
    Write-Host "You have installed `"lolcat`"..."
    Write-Host "Now Testing this command ...`n"
    lolcat --help | lolcat
}

<#
  ===================================================================================================
  LICENSE
  ---------------------------------------------------------------------------------------------------
  Copyright © 2019 Sidney ZHang <zly@lyzhang.me>

  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
  associated documentation files (the “Software”), to deal in the Software without restriction, including 
  without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
  copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
  following conditions:

  The above copyright notice and this permission notice shall be included in all copies or substantial 
  portions of the Software.
  
  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
  LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN 
  NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
  ===================================================================================================
#>