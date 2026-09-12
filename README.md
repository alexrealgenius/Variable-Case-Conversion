<h1 align="center"> Variable Case Conversion</h1>

<h2>Requirements</h2>
<ul>
  <li>Python 3.10+ (uses <code>match</code>/<code>case</code> syntax, which requires 3.10 or later)</li>
  <li><code>rapidfuzz</code></li>
</ul>

<h2>Installation</h2>
<pre><code>pip install rapidfuzz</code></pre>

<h2>Usage:</h2>

<ul>
  <li>Enter the casing convention to convert <b><i>to.</i></b></li>
  <code>Example inputs:</code>
    <ul>
      <li>camel</li>
      <li>pascal</li>
      <li>snake</li>
    </ul>
  
<br>
<br>


    
<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Target Case</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>"camelCase might-be-kebab-case"</code></td>
      <td>camel</td>
      <td><code>mightBeKebabCase
camelCase</code></td>
    </tr>
    <tr>
      <td><code>"PascalCase &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; AverageProfessors"</code></td>
      <td>snake</td>
      <td><code>my_variable_name</code></td>
    </tr>
    <tr>
      <td><code>snake_case CertainlyPascalCase</code></td>
      <td>pascal</td>
      <td><code>MyVariableName</code></td>
    </tr>
  </tbody>
</table>
