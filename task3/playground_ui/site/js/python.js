var codeInput;
var codeOutput;
var loader;

var defaultTheme = 'chalk'
var defaultPython = `# Welcome to the Python Explorer
import random;

firstRandom = random.randint(1, 100);
secondRandom = random.randint(1, 100);

sum = firstRandom + secondRandom;

print ("The first random number is: " + str(firstRandom));
print ("The second random number is: " + str(secondRandom));

print ("The sum of the random numbers is: " + str(sum));
`;

var defaultOutput = `Python Output\n`;

var separator = `˃˃ \n`;

function switch_themes(t){
    var codeInputText = $("#code")[0];
    var current_data = codeInput.getDoc().getValue();
    codeInput = CodeMirror.fromTextArea(codeInputText, {
          mode: "python",
          lineNumbers: true,
          theme: t,
          lineWrapping: true
      });
    codeInput.setValue(current_data);

    loader.attr("class","loader cm-s-"+t+"-loader");
}

function append(code_mirror, replacement_text){
  lastLine = code_mirror.getDoc().lineCount();
  code_mirror.getDoc().replaceRange(replacement_text,{line:lastLine,ch:0},{line:lastLine,ch:0})
}

function postQuery(code) {
  $.post( "/python", {code: code})

  .done(function(data) {
    response = ($.type(data) === "object")
          ? data
          : JSON.parse(data);

    append(codeOutput, response.stdout+"\n");

    console.log(response);

    if (response.stderr) {
      startLine = codeOutput.getDoc().lineCount() - 1;
      append(codeOutput, response.stderr+"\n");
      endLine = codeOutput.getDoc().lineCount();

      console.log("Start: ",startLine);
      console.log("End: ",endLine);
      codeOutput.getDoc().markText({line:startLine,ch:0},{line:endLine,ch:0}, {className:"cm-error"});

      console.log("SHOWING ERR " + response.stderr);
    }

    append(codeOutput, separator);

    loader.hide();
  })

  .fail(function( data ) {
    console.log("FAILED");
    console.log( data );

    alert("FAILED - "+data);

    loader.hide();
  });
};

window.onload = function() {

  $('#run_btn').click(function(e) {
      loader.show();

      code = codeInput.getValue();

      postQuery(code);
  });

  $('#clear_btn').click(function(e) {
      codeOutput.setValue(defaultOutput + separator)
  });

  // Set up CodeMirror
  var codeInputText = $("#code")[0];
  var codeOutputText = $("#output")[0];

  codeInput = CodeMirror.fromTextArea(codeInputText, {
      mode: "python",
      lineNumbers: true,
      theme: 'chalk',
      lineWrapping: true
  });

  codeOutput = CodeMirror.fromTextArea(codeOutputText, {
      mode: "x-sh",
      lineNumbers: false,
      theme: "console",
      readOnly: true,
      lineWrapping: true
  });

  codeInput.setValue(defaultPython);
  codeOutput.setValue(defaultOutput + separator);

  // Set up the run button loader
  loader = $('.loader')
  loader.attr("class","loader cm-s-"+defaultTheme+"-loader");
}
