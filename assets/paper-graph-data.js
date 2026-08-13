/* Canonical-homepage bootstrap: preserve the historical paper catalogue as a separate data source. */
(function(){
  'use strict';
  var nativeFetch = window.fetch.bind(window);
  window.fetch = function(input, init){
    try {
      var url = typeof input === 'string' ? input : (input && input.url ? input.url : '');
      if (url === 'index.html' || url === './index.html' || /\/NLOS_Overview\/index\.html(?:[?#].*)?$/.test(url)) {
        return nativeFetch('data/papers-source.html', init);
      }
    } catch (_) {}
    return nativeFetch(input, init);
  };
  document.write('<script src="assets/paper-graph-data-core.js"><\/script>');
})();
