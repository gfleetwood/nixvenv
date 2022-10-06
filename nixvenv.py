python = """
with import <nixpkgs> {};
let
  my-python-packages = python-packages: [
    python-packages.pip
  ];
  my-python = python310.withPackages my-python-packages;
in
  pkgs.mkShell {
    buildInputs = [
      bashInteractive
      my-python
    ];
    shellHook = ''
      export PIP_PREFIX="$(pwd)/_build/pip_packages"
      export PYTHONPATH="$(pwd)/_build/pip_packages/lib/python3.6/site-packages:$PYTHONPATH" 
      unset SOURCE_DATE_EPOCH
    '';
  }
"""

r = """
with import <nixpkgs> {};

let my-r = rWrapper.override {
packages = with rPackages; [ tidyverse ];
};

in  

pkgs.mkShell {
buildInputs = [bashInteractive my-r];
shellHook = ''
mkdir -p "$(pwd)/_libs"
export R_LIBS_USER="$(pwd)/_libs"
'';
}
"""
