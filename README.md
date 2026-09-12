<h1 align="center"> Variable Case Conversion</h1>

<br>
<br>
<p1>This project converts a string of variables to a desired case convention.</p1>
<br>
<br>
<br>


<h2>Requirements</h2>
<ul>
  <li>Python 3.10+ (uses <code>match</code>/<code>case</code> syntax, which requires 3.10 or later)</li>
  <li><code>rapidfuzz</code></li>
</ul>

<h2>Installation</h2>
<pre><code>pip install rapidfuzz</code></pre>

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


