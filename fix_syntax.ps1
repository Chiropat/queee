$mainTsPath = "c:\personal-proyects\queee\main.ts"
$content = Get-Content -Path $mainTsPath -Raw

# Corregir el error de sintaxis - reemplazar "function pez_espada () {) {" con "function pez_espada () {"
$fixedContent = $content -replace "function pez_espada \(\) \{\) \{", "function pez_espada () {"

# Guardar el contenido corregido
Set-Content -Path $mainTsPath -Value $fixedContent

Write-Host "Sintaxis corregida en main.ts"
