<#
    ====================================================================================================
                _    _    _
     ___   ___ | |_ | |_ (_) _ __    __ _
    / __| / _ \| __|| __|| || '_ \  / _` |
    \__ \|  __/| |_ | |_ | || | | || (_| |
    |___/ \___| \__| \__||_||_| |_| \__, |
                                    |___/
    ====================================================================================================
#>

$FilePlace = "C:\Users\alfch\AppData\StaticData\secretwords.json"

function Get-ObjectMembers {
    [CmdletBinding()]
    Param(
        [Parameter(Mandatory=$True, ValueFromPipeline=$True)]
        [PSCustomObject]$obj
    )
    $obj | Get-Member -MemberType NoteProperty | ForEach-Object {
        $key = $_.Name
        [PSCustomObject]@{Key = $key; Value = $obj."$key"}
    }
}

Export-ModuleMember -Function Get-ObjectMembers

function Get-SecretWords {
    Param(
        [Parameter(Mandatory=$True)]
        [Alias("w")]
        [String] $SearchWords,
        [ValidateSet("inline","cli","all")]
        [Alias("m")]
        $Mode = "inline"
    )
    begin {
        if (Test-Path $FilePlace) {
            $Full_Data = Get-Content $FilePlace | ConvertFrom-Json
        } else {
            Write-Host "`tThis"
        }
        if ($Mode -eq "inline") {
            if ($SearchWords.Contains("-")) {
                $commandlist = $SearchWords -split "-"
            } else {
                $commandlist = $SearchWords
            }
        } elseif ($Mode -eq "cli") {
            if () {
                Write-Host ""
            }
        } elseif ($Mode -eq "all") {
            #h
        } else {
            Write-Host ""
        }
    }
    process {
        #h
    }
    end {
        #gg
    }
}