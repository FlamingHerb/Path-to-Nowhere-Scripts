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


</script>

<span>Initial Level:</span>
<input bind:value={initial_level}/>

<span>Goal Level:</span>
<input bind:value={goal_level}/>

<span>Sinner Class:</span>
<input bind:value={refreshes}/>

<h1>Discoins Need</h1>
<h2>{Mania['s'][goal_level] - Mania['s'][initial_level]}</h2>
