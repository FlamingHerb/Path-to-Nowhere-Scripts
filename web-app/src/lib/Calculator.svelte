<script>
    import CardImage from '$lib/CardImage.svelte';

    import Mania from '$lib/data/mania.json';
    import Discoins from '$lib/data/discoin.json';
    import Sinners from '$lib/data/sinner.json';

    let initial_level = 1;              // Range: 1 - 89
    let goal_level = 70;                 // Range: 2 - 90
    let sinner = "Pepper";                    // For now, ignore.
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

<div class="grid grid-cols-1 md:grid-cols-[30%_70%]  h-screen">
    <div class="bg-[url(/bg/closeup.png)] bg-center ">
        <img src="profiles/{sinner.toLowerCase()}.png" alt="{sinner}'s Image" class="mx-auto">
        <!-- <h1 class="font-dflisong text-white text-center text-5xl">{sinner}</h1> -->
        <select 
            class="block font-dflisong mx-auto text-center text-5xl bg-transparent text-white border-0"
            bind:value={sinner} 
            on:change={sinnerChange}
        >
            {#each Object.keys(Sinners) as sinner}
                <option value={sinner}>
                    {sinner}
                </option>
            {/each}
        </select>
    </div>
    
    <div id="sinner-details" class="bg-black text-white ">
        <input hidden bind:value={initial_level}/>
        <input hidden bind:value={goal_level}/>

        <div class="grid grid-cols-3 grid-rows-2 mx-auto size-fit my-10">
            <p class="text-center">Initial Level</p>
            <p></p>
            <p class="text-center">Goal Level</p>

            <div class="mx-auto">
                <button class="level-up-button" on:click={decrement("init")}>-</button>
                <span class="level-up-number mx-5">{initial_level}</span>
                <button class="level-up-button" on:click={increment("init")}>+</button>
            </div>
            

            <img class="w-[32px] mx-auto" src="/bg/levelupdirection.png" alt="">

            <div class="mx-auto">
                <button class="level-up-button" on:click={decrement("goal")}>-</button>
                <span class="level-up-number mx-5">{goal_level}</span>
                <button class="level-up-button" on:click={increment("goal")}>+</button>
            </div>
            
        </div>

    
        {#if sinner == "Sinner" || sinner == ""}
            <h1>a</h1>
        {:else}
            <!-- <h1>Currency Needed:</h1> -->
            <table class="mx-auto">
                <tbody>
                    <tr>
                    <!-- DisCoins -->
                    <td>
                        <div class="mat_rarity_2">
                            <CardImage
                                mat_type        = { "currency" }
                                image_size      = { image_size }
                                sinner_mat      = { "discoin" }
                                mat_cost_rarity = { 2 }
                                mat_cost        = { Discoins[sinner_class][goal_level] - Discoins[sinner_class][initial_level] }
                            />
                        </div>
                    </td>
                    <!-- Mania -->
                    <td>
                        <div class="mat_rarity_2">
                            <CardImage
                                mat_type        = { "currency" }
                                image_size      = { image_size }
                                sinner_mat      = { "mania" }
                                mat_cost_rarity = { mat_cost_rarity[0][0] }
                                mat_cost        = { Mania[sinner_class][goal_level] - Mania[sinner_class][initial_level] }
                            />
                        </div>
                    </td>
                </tr>
                </tbody>
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
    
            <h2 class="text-3xl font-dflisong text-center">Materials Needed:</h2>
            {#if initial_level < 20 && goal_level >= 20}
                {@render phase_costs(0)}
            {/if}
            {#if initial_level < 40 && goal_level >= 40}
                {@render phase_costs(1)}
            {/if}
            {#if initial_level < 70 && goal_level >= 70}
                {@render phase_costs(2)}
            {/if}
        {/if}
    </div>
</div>


{#snippet phase_costs(current_phase)}
<h2 class="text-center font-bold text-2xl">Phase {current_phase + 1} Cost:</h2>
<div class="grid grid-cols-4 w-[260px] mx-auto">
    <CardImage
        mat_type        = { "fluid" }
        image_size      = { image_size }
        sinner_mat      = { Sinners[sinner].tendency }
        mat_cost_rarity = { mat_cost_rarity[current_phase][0]}
        mat_cost        = { mat_cost[current_phase][0] }
    />
    <CardImage
        mat_type        = { "material" }
        image_size      = { image_size }
        sinner_mat      = { Sinners[sinner].rum_1 }
        mat_cost_rarity = { mat_cost_rarity[current_phase][1] }
        mat_cost        = { mat_cost[current_phase][1] }
    />
    <CardImage
        mat_type        = { "material" }
        image_size      = { image_size }
        sinner_mat      = { Sinners[sinner].rum_2 }
        mat_cost_rarity = { mat_cost_rarity[current_phase][2] }
        mat_cost        = { mat_cost[current_phase][2] }
    />
    <CardImage
        mat_type        = { "currency" }
        image_size      = { image_size }
        sinner_mat      = { "discoin" }
        mat_cost_rarity = { 2 }
        mat_cost        = { discoin_cost[current_phase] }
    />
</div>    

{/snippet}
