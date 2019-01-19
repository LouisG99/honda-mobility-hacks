<!DOCTYPE html>
<html lang="en">>
    <head>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }

            table, td, th {
                border: 1px solid black;
                padding: 5px;
            }

            th {text-align: left;}
        </style>
    </head>
<body>

    <?php
        echo "<html><body><table>\n\n";
        $f = fopen("test.csv", "r");
        while (($line = fgetcsv($f)) !== false) {
            echo "<tr>";
            $counter_int = 0;
            $num_cols = 3;
            foreach ($line as $cell) {
                if ($counter_int == 0) {
                    if (htmlspecialchars($cell) == '1') {
                        echo "<td bgcolor=\"#00FF00\">" . htmlspecialchars($cell) . "</td>";
                    }
                    else if (htmlspecialchars($cell) == '2') {
                        echo "<td bgcolor=\"#FFFF00\">" . htmlspecialchars($cell) . "</td>";
                    }
                    else if (htmlspecialchars($cell) == '3') {
                        echo "<td bgcolor=\"#FF0000\">" . htmlspecialchars($cell) . "</td>";
                    }
                    else {
                        echo "<td>" . htmlspecialchars($cell) . "</td>";
                    }
                }
                else {
                    echo "<td>" . htmlspecialchars($cell) . "</td>";
                }
                $counter_int += 1;
            }
            echo "</tr>\n";
        }
       
        
        echo "\n</table></body></html>";


    ?>
</body>
</html>