# fvwm-menu-desktop
Creates application menu for fvwm3 desktop

Running `fvwm-menu-desktop -e` on NetBSD (and OpenBSD for that matter) produces this,

```bash
DestroyMenu "XDGMenu"
AddToMenu "XDGMenu" "XDGMenu" Title
+ "$[gt.Error]: $[gt.No menus found]" Nop
+ "" Nop
+ "$[gt.Regenerate]" PipeRead `fvwm-menu-desktop -e`
```

I'm going to try to rewrite fvwm-menu-desktop so that at least it works for NetBSD

