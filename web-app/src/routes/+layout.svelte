<script>
  import "../app.scss";
  /** @type {{children?: import('svelte').Snippet}} */
  let { children } = $props();
</script>

{@render children?.()}
