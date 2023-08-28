<script>
</script>

<div class="matcard">
    <slot />
</div>

<style lang="scss">
    .matcard {
        position: relative;
        border: 1px solid #000;
        max-height: 128px;
        max-width: 128px;
    }
    .matcard :global(> :last-child) {
        position:absolute;
        bottom:0;
        right:0;
    }
</style>

