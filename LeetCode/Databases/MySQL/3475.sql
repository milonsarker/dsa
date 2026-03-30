#https://leetcode.com/problems/dna-pattern-recognition/description/

# Write your MySQL query statement below

select  sample_id, dna_sequence, species, 
        REGEXP_LIKE(dna_sequence,'^ATG', 'c') has_start, 
        REGEXP_LIKE(dna_sequence,'(TAA|TAG|TGA)$', 'c') has_stop, 
        REGEXP_LIKE(dna_sequence,'(ATAT)+', 'c') has_atat, 
        REGEXP_LIKE(dna_sequence,'[G]{3,}', 'c') has_ggg
    from samples;


#REGEXP_LIKE(description,'(^|[^A-Za-z0-9])SN[0-9]{4}-[0-9]{4}([^A-Za-z0-9]|$)', 'c')
