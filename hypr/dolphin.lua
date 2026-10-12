-- Hyprland (config em Lua) — regras para o Dolphin
-- A translucidez vem do Darkly (darklyrc); o Hyprland mantém a janela opaca
-- e só faz blur onde o Darkly deixa passar.
hl.window_rule({ match = { class = "^(org\\.kde\\.dolphin)$" }, opacity = "1.0 override" })

-- Diálogos do Dolphin a flutuar (en + pt)
hl.window_rule({
    match = {
        class = "^(org\\.kde\\.dolphin)$",
        title = "^(Moving.*|A\\smover.*|Create New.*|Criar\\sNovo.*|Extract.*|Extrair.*|Compress.*|Comprimir.*|Copying.*|A\\scopiar.*|Progress.*|Configure.*|Configurar.*|Properties.*|Propriedades.*|Choose\\sApplication.*|Escolha\\sAplica.*)$",
    },
    float  = true,
    center = true,
})

-- IMPORTANTE: não usar scale < 1 no monitor (ex.: 0.9375).
-- O blur do Hyprland fica recortado em (largura*scale, altura*scale).
-- hl.monitor({ output = "eDP-1", mode = "preferred", scale = "1" })
