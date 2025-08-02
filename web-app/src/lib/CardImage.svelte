<script>
    /** @type {{children?: import('svelte').Snippet}} */
    let { children } = $props();
</script>


<div class="matcard ">
    {@render children?.()}
</div>

<style lang="scss">
    

    .matcard {
        background-color: #000;
        position: relative;
        max-height: 64px;
        max-width: 64px;
    }

    .matcard :global(.mat_overlay) {
        position: absolute;
        top: 0;
    }

    .matcard :global(span) {
        font-family: 'HYQiHeiB5-55';
        font-size: 0.6rem;
        position:absolute;
        background-color: rgba(0,0,0,0.69);
        color: #fff;
        text-align: right;
        width: 62px;
        padding-right: 2px;
        bottom:0;
        right:0;
    }
</style>

