import compileall

print("Compiling application to bytecode...")

success = compileall.compile_dir(
    "app",
    force=True,
    quiet=1,
)

if success:
    print("Compilation successful.")
else:
    print("Compilation failed.")
    raise SystemExit(1)
