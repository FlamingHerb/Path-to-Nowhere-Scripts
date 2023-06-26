<script>
    import Mania from '$lib/data/mania.json';
    import Discoins from '$lib/data/discoin.json';
    import Sinners from '$lib/data/sinner.json';

    let initial_level = 1;              // Range: 1 - 89
    let goal_level = 2;                 // Range: 2 - 90
    let sinner = "Sinner";                    // For now, ignore.
    let sinner_class = "b";
    let refreshes = 0;                  // Range: 0 - 10
    let black_key_available = false;
    let mat_cost = [[12,30,15],[12,30,15],[20,54,30]];
    let mat_cost_rarity = [[1,1,1],[2,2,2],[3,3,3]];

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
                break;
            case "a":
                mat_cost = [[15,12,18],[15,12,18],[25,24,36]];
                mat_cost_rarity = [[1,2,1],[2,3,2],[3,4,3]];
                break;
            case "b":
                mat_cost = [[12,30,15],[12,30,15],[20,54,30]];
                mat_cost_rarity = [[1,1,1],[2,2,2],[3,3,3]];
                break;
        }
    }

</script>

<span>Initial Level:</span>
<input bind:value={initial_level}/>
<button on:click={increment("init")}>Plus</button>
<button on:click={decrement("init")}>Minus</button>
<br>

<span>Goal Level:</span>
<input bind:value={goal_level}/>
<button on:click={increment("goal")}>Plus</button>
<button on:click={decrement("goal")}>Minus</button>
<br>

<!-- <select bind:value={sinner_class}>
    <option value="s">s</option>
    <option value="a">a</option>
    <option value="b">b</option>
</select> -->

{sinner_class}

<select bind:value={sinner} on:change={sinnerChange}>
    {#each Object.keys(Sinners) as sinner}
        <option value={sinner}>
            {sinner}
        </option>
    {/each}
</select>

<h1>Discoins Needed</h1>
<h2>{Discoins[sinner_class][goal_level] - Discoins[sinner_class][initial_level]}</h2>

{#if initial_level < 20 && goal_level >= 20}
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
{/if}

<h1>Mania Needed Needed</h1>
<h2>{Mania[sinner_class][goal_level] - Mania[sinner_class][initial_level]}</h2>

<h1>Materials Needed</h1>
{#if initial_level < 20 && goal_level >= 20}
    <ul>Phase 1 Cost:
        <li><img src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[0][0]}.png"></li>
    </ul>
{/if}
{#if initial_level < 40 && goal_level >= 40}
    <ul>Phase 2 Cost:
        <li><img src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[1][0]}.png"></li>
    </ul>
{/if}
{#if initial_level < 70 && goal_level >= 70}
    <ul>Phase 2 Cost:
        <li><img src="fluid/{Sinners[sinner].tendency}_{mat_cost_rarity[2][0]}.png"></li>
    </ul>
{/if}