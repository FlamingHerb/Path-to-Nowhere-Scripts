<script>
    import CardImage from '$lib/CardImage.svelte';

    import Mania from '$lib/data/mania.json';
    import Discoins from '$lib/data/discoin.json';
    import Sinners from '$lib/data/sinner.json';

    let initial_level = 1;              // Range: 1 - 89
    let goal_level = 70;                 // Range: 2 - 90
    let sinner = "Sinner";                    // For now, ignore.
    let sinner_class = "b";
    let refreshes = 0;                  // Range: 0 - 10
    let black_key_available = false;
    let mat_cost = [[12,30,15],[12,30,15],[20,54,30]];
    let mat_cost_rarity = [[1,1,1],[2,2,2],[3,3,3]];
    let discoin_cost = [24000,80000,350000];
    let image_size = 64;

    const increment = varName => () => {
        switch(varName){
            case "init":
                if (initial_level < goal_level - 1){
                    initial_level += 1;
                }
                break;
            case "goal":
                if (goal_level < 90){
                    goal_level += 1;
                }
                break;
        }
    }

    const decrement = varName => () => {
        switch(varName){
            case "init":
                if (initial_level > 1){
                    initial_level -= 1;
                }
                break;
            case "goal":
                if (initial_level < goal_level - 1){
                    goal_level -= 1;
                }
                break;
        }
    }

    const sinnerChange = () => {
        sinner_class = Sinners[sinner].rank;
        switch(sinner_class){
            case "s":
                mat_cost = [[18,16,8],[18,16,8],[30,28,15]];
                mat_cost_rarity = [[1,2,2],[2,3,3],[3,4,4]];
                discoin_cost = [36000,120000,560000];
                break;
            case "a":
                mat_cost = [[15,12,18],[15,12,18],[25,24,36]];
                mat_cost_rarity = [[1,2,1],[2,3,2],[3,4,3]];
                discoin_cost = [30000,100000,480000];
                break;
            case "b":
                mat_cost = [[12,30,15],[12,30,15],[20,54,30]];
                mat_cost_rarity = [[1,1,1],[2,2,2],[3,3,3]];
                discoin_cost = [24000,80000,350000];
                break;
        }
    }

</script>

<div id="sinner-selection">
    <img src="profiles/{sinner.toLowerCase()}.png" alt="">
    <h1>{sinner}</h1>
    <select bind:value={sinner} on:change={sinnerChange}>
        {#each Object.keys(Sinners) as sinner}
            <option value={sinner}>
                {sinner}
            </option>
        {/each}
    </select>
</div>

<div id="sinner-details">
    <input hidden bind:value={initial_level}/>
    <input hidden bind:value={goal_level}/>

    <table id="level-up-prompt" style="margin: auto;">
        <tr>
            <td colspan="3">
                Initial Level
            </td>
            <td>

            </td>
            <td colspan="3">
                Goal Level
            </td>
        </tr>
        <!-- Numbers and transition-->
        <tr>
            <td>
                <button class="level-up-button" on:click={decrement("init")}>-</button>
            </td>
            <td>
                <span class="level-up-number">{initial_level}</span>
            </td>
            <td>
                <button class="level-up-button" on:click={increment("init")}>+</button>
            </td>

            <td>
                <img width="32px" src="/bg/levelupdirection.png" alt="">
            </td>

            <td>
                <button class="level-up-button" on:click={decrement("goal")}>-</button>
            </td>
            <td>
                <span class="level-up-number">{goal_level}</span>
            </td>
            <td>
                <button class="level-up-button" on:click={increment("goal")}>+</button>
            </td>
        </tr>
    </table>

    {#if sinner == "Sinner" || sinner == ""}
        <h1>a</h1>
    {:else}
        <!-- <h1>Currency Needed:</h1> -->
        <table>
            <tr>
                <td>
                    <div class="mat_rarity_2">
                        <CardImage>
                            <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_2.png" alt="">
                            <img style="width: {image_size}px" src="currency/discoin.png" alt="">
                            <span>{Discoins[sinner_class][goal_level] - Discoins[sinner_class][initial_level]}</span>
                        </CardImage>
                    </div>
                </td>
                <td>
                    <div class="mat_rarity_2">
                        <CardImage>
                            <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_2.png" alt="">
                            <img style="width: {image_size}px" src="currency/mania.png" alt="">
                            <span>{Mania[sinner_class][goal_level] - Mania[sinner_class][initial_level]}</span>
                        </CardImage>
                    </div>
                </td>
            </tr>
        </table>

        <!-- {#if initial_level < 20 && goal_level >= 20}
            <h2>Phase 1 Cost:
                {#if sinner_class == "b"}
                    24000
                {:else if sinner_class == "a"}
                    30000
                {:else if sinner_class == "s"}
                    36000
                {/if}
            </h2>
        {/if}
        {#if initial_level < 40 && goal_level >= 40}
            <h2>Phase 2 Cost:
                {#if sinner_class == "b"}
                    80000
                {:else if sinner_class == "a"}
                    100000
                {:else if sinner_class == "s"}
                    120000
                {/if}
            </h2>
        {/if}
        {#if initial_level < 70 && goal_level >= 70}
            <h2>Phase 3 Cost:
                {#if sinner_class == "b"}
                    350000
                {:else if sinner_class == "a"}
                    480000
                {:else if sinner_class == "s"}
                    560000
                {/if}
            </h2>
        {/if} -->

        <h1>Materials Needed:</h1>
        {#if initial_level < 20 && goal_level >= 20}
            <table>
                <tr>
                    <th colspan="4">Phase 1 Cost:</th>
                </tr>
                <tr>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[0][0] + 1}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px;" src="rarity/rarity_{mat_cost_rarity[0][0] + 1}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[0][0]}.png" alt="">
                                <span>{mat_cost[0][0]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[0][1]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[0][1]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_1}_{mat_cost_rarity[0][1]}.png" alt="">
                                <span>{mat_cost[0][1]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[0][2]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[0][2]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_2}_{mat_cost_rarity[0][2]}.png" alt="">
                                <span>{mat_cost[0][2]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_2">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_2.png" alt="">
                                <img style="width: {image_size}px" src="currency/discoin.png" alt="">
                                <span>{discoin_cost[0]}</span>
                            </CardImage>
                        </div>
                    </td>
                </tr>
            </table>
        {/if}
        {#if initial_level < 40 && goal_level >= 40}
            <table>
                <tr>
                    <th colspan="4">Phase 2 Cost:</th>
                </tr>
                <tr>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[1][0] + 1}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[1][0] + 1}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[1][0]}.png" alt="">
                                <span>{mat_cost[1][0]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[1][1]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[1][1]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_1}_{mat_cost_rarity[1][1]}.png" alt="">
                                <span>{mat_cost[1][1]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[1][2]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[1][2]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_2}_{mat_cost_rarity[1][2]}.png" alt="">
                                <span>{mat_cost[1][2]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_2">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_2.png" alt="">
                                <img style="width: {image_size}px" src="currency/discoin.png" alt="">
                                <span>{discoin_cost[1]}</span>
                            </CardImage>
                        </div>
                    </td>
                </tr>
            </table>
        {/if}
        {#if initial_level < 70 && goal_level >= 70}
            <table>
                <tr>
                    <th colspan="4">Phase 3 Cost:</th>
                </tr>
                <tr>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[2][0] + 1}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[2][0] + 1}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[2][0]}.png" alt="">
                                <span>{mat_cost[2][0]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[2][1]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[2][1]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_1}_{mat_cost_rarity[2][1]}.png" alt="">
                                <span>{mat_cost[2][1]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_{mat_cost_rarity[2][2]}">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_{mat_cost_rarity[2][2]}.png" alt="">
                                <img class="mat_overlay" style="width: {image_size}px" src="material/material_overlay.png" alt="">
                                <img style="width: {image_size}px" src="material/{Sinners[sinner].rum_2}_{mat_cost_rarity[2][2]}.png" alt="">
                                <span>{mat_cost[2][2]}</span>
                            </CardImage>
                        </div>
                    </td>
                    <td>
                        <div class="mat_rarity_2">
                            <CardImage>
                                <img class="mat_overlay" style="width: {image_size}px" src="rarity/rarity_2.png" alt="">
                                <img style="width: {image_size}px" src="currency/discoin.png" alt="">
                                <span>{discoin_cost[2]}</span>
                            </CardImage>
                        </div>
                    </td>
                </tr>
            </table>
        {/if}
    {/if}
</div>



<style lang="scss">
    :global(body) {
        font-family: 'Pretendard Medium';
        background: url("/bg/closeup.png");
        background-position-x: center;
        background-position-y: top;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        color: white;

        margin: 0px;
    }

    #sinner-selection {
        text-align: center;

        img {
            width: 300px;
            height: 200px;
            
            object-fit: cover;
            object-position: top;
        }

        h1 {
            margin-top: -50px;
            font-family: 'DFLiSong Std W7';
        }

    }

    #sinner-details {
        padding: 8px;
        width: 100%;
        min-height: 70vh;
        background-color: black;
    }

    .level-up-button {
        background-color: transparent !important;
        font-family: 'Pretendard Medium';
        font-size: 24px;
        color: #9EAAC3;
        border: none;
    }

    .level-up-number {
        font-family: 'Pretendard Medium';
        font-size: 40px;

    }

    #level-up-prompt {
        text-align: center;

        td {
            width: 50px;
        }
    }

    .mat_rarity_1 {
        border: 1px solid #9EAAC3;
        border-bottom-width: 2px;
        border-radius: 1px;
    }
    .mat_rarity_2 {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(#9EAAC3, #9EAAC3, #4CD5A3) 1;
        // border: 2px solid #4CD5A3;
        border-bottom-width: 2px;
        border-radius: 1px;
    }
    .mat_rarity_3 {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(#9EAAC3, #9EAAC3, #75AAF1) 1;
        // border: 2px solid #75AAF1;
        border-bottom-width: 2px;
        border-radius: 1px;
    }
    .mat_rarity_4 {
        border-width: 1px;
        border-style: solid;
        border-image: linear-gradient(#9EAAC3, #9EAAC3, #F1AEFF) 1;
        // border: 2px solid #F1AEFF;
        border-bottom-width: 2px;
        border-radius: 1px;
    }
</style>