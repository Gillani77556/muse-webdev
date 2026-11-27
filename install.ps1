# Muse WebDev installer (Windows). Run ONLY after cloning this repo yourself.
$SkillDir = "$env:USERPROFILE\.claude\skills\webdev"
$AgentDir = "$env:USERPROFILE\.claude\agents"
New-Item -ItemType Directory -Force -Path $SkillDir, $AgentDir | Out-Null
Copy-Item -Recurse -Force "skills\webdev\*" $SkillDir
Get-ChildItem "skills" -Directory | ForEach-Object {
  $t = "$env:USERPROFILE\.claude\skills\$($_.Name)"
  New-Item -ItemType Directory -Force -Path $t | Out-Null
  Copy-Item -Recurse -Force "$($_.FullName)\*" $t
}
Copy-Item -Force "agents\*.md" $AgentDir
# Copy shared scripts + launcher — hub runs checks via skills\webdev\scripts\webdev
New-Item -ItemType Directory -Force -Path "$SkillDir\scripts" | Out-Null
Copy-Item -Recurse -Force "scripts\*" "$SkillDir\scripts"
Write-Host "Done. Check: $SkillDir\scripts\webdev doctor"
