<# -------------------------------------------------------------------------------------------------
  _ __                                     _            _  _  _ __                 __  _  _
  | '_ \   ___  __      __  ___  _ __  ___ | |__    ___ | || || '_ \  _ __   ___   / _|(_)| |  ___
  | |_) | / _ \ \ \ /\ / / / _ \| '__|/ __|| '_ \  / _ \| || || |_) || '__| / _ \ | |_ | || | / _ \
  | .__/ | (_) | \ V  V / |  __/| |   \__ \| | | ||  __/| || || .__/ | |   | (_) ||  _|| || ||  __/
  |_|     \___/   \_/\_/   \___||_|   |___/|_| |_| \___||_||_||_|    |_|    \___/ |_|  |_||_| \___|
  ------------------------------------------------------------------------------------------------- #>
# Coding by Sidney Zhang <zly@lyzhang.com>
# Update 2019-11-09

<#
  ===================================================================================================
  REQUIRED MODULES
  ===================================================================================================
#>

Import-Module PSColor
Import-Module PlusGeneral
If (-Not (Test-Path Variable:PSise)) { # Only run this in the console and not in the ISE
    Import-Module Get-ChildItemColor
}
Import-Module posh-git
Import-Module oh-my-posh
Import-Module windows-Screenfetch

<#
  ===================================================================================================
  STATIC VARIABLES
  ===================================================================================================
#>

New-Variable -Name Download -Value ($HOME + "\Downloads") -Option Constant -Description "This is download folder."
New-Variable -Name APPDATA -Value ($HOME + "\AppData") -Option Constant -Description "This is appdata folder."
New-Variable -Name CODE -Value "<your coding folder>" -Option Constant -Description "This is my coding work folder."

<#
  ===================================================================================================
  FUNCTIONS
  ===================================================================================================
#>
<# --------------------------------------------General--------------------------------------------- #>

function x { exit }
function MyPublicIP { (Get-MyIPAddress).IPAddress }
function MyLANIP
{
    $infoIP = (Get-MyIPAddress -Mode "inner" -All)[0]
    $res = @($infoIP.IPv6LinkLocalAddress.IPAddress,$infoIP.IPv4Address.IPAddress)
    return $res
}
function figlet { Write-Ascii $args -Fore Green }
function weather { GET-NowWeather -s -userkey "<your appkey>" }
function print_weather { GET-NowWeather -userkey "<your appkey>" }

<# -------------------------------------------Location--------------------------------------------- #>

function Set-coding { Set-Location $CODE }
function Set-download { Set-Location $Download }
function Set-AppData { Set-Location $APPDATA }

<# ----------------------------------------------Git----------------------------------------------- #>

function Get-gitadd
{
    git add .
    git commit -m $args
}

function Get-gitpush { git push -u origin master }

function Get-gitget
{
    param(
      [ValidateSet("clone","pull","fetch")]
      [Alias("m")]
      $Mode = "pull",
      [String]
      [Alias("b")]
      $Branch = "master",
      [String]
      [Alias("s")]
      $Server = "origin",
      [String]
      [Alias("t")]
      $ownBranch = "master"
    )
    switch ($Mode) {
      "clone" {
        git clone $args
        break
      }
      "pull" {
        git pull $Server $Branch
        break
      }
      "fetch" {
        $to = $Branch + ":" +$ownBranch
        git fetch $Server $to
        Break
      }
    }
}
<#
  ===================================================================================================
  ALIASES
  ===================================================================================================
#>

Set-Alias -Name pubIP -Value MyPublicIP
Set-Alias -Name lanIP -Value MyLANIP
Set-Alias -Name cc -Value CloseComputer
Set-Alias -Name ss -Value StopShutdown
Set-Alias -Name rcc -Value RestartComputer
Set-Alias -Name opa -Value Open-PowershellAdmin
Set-Alias -Name opca -Value Open-PowershellCoreAdmin
Set-Alias -Name pipy -Value Start-pip
Set-Alias -Name prwt -Value print_weather
Set-Alias -Name cdco -Value Set-coding
Set-Alias -Name cddo -Value Set-download
Set-Alias -Name cdad -Value Set-AppData
Set-Alias -Name ga -Value Get-gitadd
Set-Alias -Name gip -Value Get-gitpush
Set-Alias -Name gg -Value Get-gitget


<#
  ===================================================================================================
  SETTING CONSOLE
  ===================================================================================================
#>

Set-Theme PowerLine
Screenfetch
weather | lolcat
Write-Host "`n"
Get-WelcomeScreen "Sidney"

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