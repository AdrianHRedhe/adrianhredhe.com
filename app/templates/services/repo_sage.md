## RepoSage

I created a cli which can clone and sync a github users public repos, and build
a local chunk-aware knowledge base to answer questions about their code, with
an LLM synthesizing answers cited back to repo/file/line. 

Here you can test it out on my public repos and ask any questions you may have.
You can bring your own public repo through the sandbox tab.
Or clone it yourself to run it as a cli with a local llm on your own computer.

Source: [repo-sage on GitHub](https://github.com/AdrianHRedhe/repo-sage).

<div class="repo-sage-embed">
<iframe id="repo-sage-iframe" src="https://repo-sage.adrianhredhe.com/" title="RepoSage" width="100%" height="500" frameborder="0"></iframe>
</div>

<style>
.repo-sage-embed {
  margin-top: 1rem;
}

.repo-sage-embed iframe {
  display: block;
  width: 100%;
  border: none;
  /* Starting height, covering the embedded app before it's reported
     its real size (see script below) - just enough for its
     pre-interaction state so there's no flash of empty space. */
  height: 500px;
}
</style>

<script>
// The embedded RepoSage app posts its actual content height (it grows
// with every question asked - see its own postHeight script) so this
// iframe can always match it exactly. That avoids a scrollbar nested
// inside this page's own scrollbar: only one scrollbar ever appears,
// on this outer page, and only once the conversation genuinely
// outgrows the viewport.
(function () {
  var REPO_SAGE_ORIGIN = "https://repo-sage.adrianhredhe.com";
  var iframe = document.getElementById("repo-sage-iframe");

  window.addEventListener("message", function (event) {
    if (event.origin !== REPO_SAGE_ORIGIN) return;
    var data = event.data;
    if (!data || data.type !== "repo-sage:height") return;
    var height = Number(data.height);
    if (Number.isFinite(height) && height > 0) {
      iframe.style.height = height + "px";
    }
  });
})();
</script>
