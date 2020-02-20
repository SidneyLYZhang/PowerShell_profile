# get secrets
# update 2020-02-17

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

function Get-Secrets {
    param(
        [Alias("p")]
        [String] $psw
    )

    python getSecret.py search by curtype $args --password $psw
}

Export-ModuleMember -Function Get-Secrets