from distutils.core import setup, Extension

setup(name='actontext', version='1.0', )

setup(
  name = 'actontext',
  packages = ['actontext'],
  version = '0.1',
  license='MIT',
  description = """This module provides functions to load COM DLL on Windows machine, to avoid registering it in Windows registry.
You can find more about how it can be done in articles on web:
- \"Registration-Free Activation of COM Components: A Walkthrough\" (https://docs.microsoft.com/en-us/previous-versions/dotnet/articles/ms973913(v=msdn.10));
- \"\" (https://weblog.west-wind.com/posts/2011/Oct/09/An-easy-way-to-create-Side-by-Side-registrationless-COM-Manifests-with-Visual-Studio);
- etc. just Google it

The main use case for module could be lightweight testing of COM objects, created from built in-proc COM servers""",
  author = 'Mokych Andrey',
  author_email = 'mokych.apriorit@gmail.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['COM', 'ATL', 'side-by-side', 'activation context'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
  ext_modules=[
      Extension('actontext_internal', ['native/actonext.cpp'])]
)