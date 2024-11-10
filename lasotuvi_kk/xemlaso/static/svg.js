prefix = {
    svg: 'http://www.w3.org/2000/svg',
    xhtml: 'http://www.w3.org/1999/xhtml',
    xlink: 'http://www.w3.org/1999/xlink',
    xml: 'http://www.w3.org/XML/1998/namespace',
    xmlns: 'http://www.w3.org/2000/xmlns/',
};

function setInlineStyles(svg) {

    // add empty svg element
    var emptySvg = window.document.createElementNS(prefix.svg, 'svg');
    window.document.body.appendChild(emptySvg);
    var emptySvgDeclarationComputed = window.getComputedStyle(emptySvg);
  
    // hardcode computed css styles inside svg
    var allElements = traverse(svg);
    var i = allElements.length;
    while (i--) {
      explicitlySetStyle(allElements[i]);
    }
  
    emptySvg.parentNode.removeChild(emptySvg);
  
    function explicitlySetStyle(element) {
      var cSSStyleDeclarationComputed = window.getComputedStyle(element);
      var i;
      var len;
      var key;
      var value;
      var computedStyleStr = '';
  
      for (i = 0, len = cSSStyleDeclarationComputed.length; i < len; i++) {
        key = cSSStyleDeclarationComputed[i];
        value = cSSStyleDeclarationComputed.getPropertyValue(key);
        if (value !== emptySvgDeclarationComputed.getPropertyValue(key)) {
          // Don't set computed style of width and height. Makes SVG elmements disappear.
          if ((key !== 'height') && (key !== 'width')) {
            computedStyleStr += key + ':' + value + ';';
          }
  
        }
      }
  
      element.setAttribute('style', computedStyleStr);
    }
  
    function traverse(obj) {
      var tree = [];
      tree.push(obj);
      visit(obj);
      function visit(node) {
        if (node && node.hasChildNodes()) {
          var child = node.firstChild;
          while (child) {
            if (child.nodeType === 1 && child.nodeName != 'SCRIPT') {
              tree.push(child);
              visit(child);
            }
  
            child = child.nextSibling;
          }
        }
      }
  
      return tree;
    }
}

function preprocess(svg) {
    svg.setAttribute('version', '1.1');
  
    // removing attributes so they aren't doubled up
    svg.removeAttribute('xmlns');
    svg.removeAttribute('xlink');
  
    // These are needed for the svg
    if (!svg.hasAttributeNS(prefix.xmlns, 'xmlns')) {
      svg.setAttributeNS(prefix.xmlns, 'xmlns', prefix.svg);
    }
  
    if (!svg.hasAttributeNS(prefix.xmlns, 'xmlns:xlink')) {
      svg.setAttributeNS(prefix.xmlns, 'xmlns:xlink', prefix.xlink);
    }
  
    setInlineStyles(svg);
  
    var xmls = new XMLSerializer();
    var source = xmls.serializeToString(svg);
    var doctype = '<?xml version="1.0" standalone="no"?><!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">';
    var rect = svg.getBoundingClientRect();
    var svgInfo = {
      top: rect.top,
      left: rect.left,
      width: rect.width,
      height: rect.height,
      class: svg.getAttribute('class'),
      id: svg.getAttribute('id'),
      childElementCount: svg.childElementCount,
      source: [doctype + source],
    };
  
    return svgInfo;
}

