<script>
    import Mania from '$lib/data/mania.json';
    import Discoins from '$lib/data/discoin.json';

    let initial_level = 1;              // Range: 1 - 89
    let goal_level = 2;                 // Range: 2 - 90
    let sinner = "";                    // For now, ignore.
    let sinner_class = "b";
    let refreshes = 0;                  // Range: 0 - 10
    let black_key_available = false;
    let phase_cost_yes = false;

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

<select bind:value={sinner_class}>
    <option value="s">s</option>
    <option value="a">a</option>
    <option value="b">b</option>
</select>

<h1>Discoins Needed</h1>
<h2>{Discoins[sinner_class][goal_level] - Discoins[sinner_class][initial_level]}</h2>

<h1>Mania Needed Needed</h1>
<h2>{Mania[sinner_class][goal_level] - Mania[sinner_class][initial_level]}</h2>
