<h1 align="center"> Variable Case Conversion</h1>

<br>
<br>
<p1>This project converts a string of variables to a desired case convention.</p1>
<br>
<br>
<br>

<video src="assets/Python Case Converter Demo.mp4"></video>




<h2>Requirements</h2>
<ul>
  <li>Python 3.10+ (uses <code>match</code>/<code>case</code> syntax, which requires 3.10 or later)</li>
  <li><code>rapidfuzz</code></li>
</ul>

<h2>Installation</h2>


1. Clone the repo and move into the project folder

```bash
git clone https://github.com/alexrealgenius/Variable-Case-Conversion.git
cd Variable-Case-Conversion
```
<hr>
2. Install the required dependencies

```
pip install rapidfuzz pyperclip
```
if the above doesn't work, do:
```
py -m pip install rapidfuzz pyperclip
```

<hr>
3. Run the script

```
python case_converter.py
```
<h2>Usage:</h2>

<ol>
  <li><b>Enter the casing convention to convert <b><i>to.</i></b></b></li>
  <h3>Example inputs:</h3>
  <ul>
    <li>"camel"</li>
    <li>"pascal"</li>
    <li>"kebab"</li>
  </ul>

<br>

 <li><b>Enter a single string of variables delimited by any number of whitespaces.</b></li>
 <h3>Example inputs:</h3>
 <ul>
    <li>"camelCase might-be-kebab-case"</li>
    <li>"PascalCase &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AverageProfessors HiImAVariable"</li>
    <li>"snake_case CertainlyPascalCase"</li>
  </ul>

  <br>

  <li><b>Optionally copy results to clipboard when prompted.</b></li>
  </ol>
  
  <h2 align="center">Example Cases</h2>
    
<table align="center">
  <thead>
    <tr>
      <th>Input</th>
      <th>Target Case</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><code>"camelCase might-be-kebab-case"</code></td>
      <td align="center">camel</td>
      <td align="center"><code>camelCase
mightBeKebabCase</code></td>
    </tr>
    <tr>
      <td align="center"><code>"PascalCase &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AverageProfessors HiImAVariable"</code></td>
      <td align="center">snake</td>
      <td align="center"><code>pascal_case
average_professors
hi_im_a_variable</code></td>
    </tr>
    <tr>
      <td align="center"><code>snake_case CertainlyPascalCase</code></td>
      <td align="center">pascal</td>
      <td align="center"><code>SnakeCase
CertainlyPascalCase</code></td>
    </tr>
  </tbody>
</table>

<hr>

> [!WARNING]
> Variable inputs whose casing cannot be determined will be considered "ambiguous".
> <br>
> This is why the program will prompt you to "Copy non-ambiguous results to clipboard" (successful matches).
> <br>
> <br>
> The program will provide you of a list of ambiguous inputs if any are found.
<br>

>[!TIP]
> Text copied automatically to clipboard will be delimited by newlines between each word.

<br>
<h1><b>Author</b></h1>

[Alexander Troshin](https://github.com/alexrealgenius)

[![GitHub](https://img.shields.io/badge/GitHub-alexrealgenius-181717?style=for-the-badge&logo=github)](https://github.com/alexrealgenius)




<hr>

