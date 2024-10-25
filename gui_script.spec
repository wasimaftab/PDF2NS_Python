# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui_script.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/wasim/anaconda3/envs/pdf2ns/lib/python3.10/site-packages/pinecone', 'pinecone'), ('/home/wasim/Desktop/PDF2NS_python/grobid_client_python/*', './grobid_client_python/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='gui_script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='gui_script',
)
