<script>
    /** @type {{children?: import('svelte').Snippet}} */
    let {
        mat_type,
        image_size,
        sinner_mat,
        mat_cost_rarity,
        mat_cost
    } = $props();
</script>


<div class="matcard">
    <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{ mat_type == "fluid" ? mat_cost_rarity + 1 : mat_cost_rarity }.png" alt="">
    {#if mat_type == "currency"}
        <img style="width: {image_size}px" src="currency/{sinner_mat}.png" alt="">
    {/if}
    {#if mat_type == "material"}
        <img style="width: {image_size}px" src="material/{sinner_mat}_{mat_cost_rarity}.png" alt="">
    {/if}
    {#if mat_type == "fluid"}
        <img style="width: {image_size}px" src="fluid/{sinner_mat}_{mat_cost_rarity}.png" alt="">
    {/if}
    {#if mat_type != "currency"}
        <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
    {/if}

    <span>{mat_cost}</span>

</div>

<style>
    

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

